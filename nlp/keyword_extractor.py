import yake
import numpy as np
from transformers import AutoTokenizer
import onnxruntime as ort
import json

tokenizer = AutoTokenizer.from_pretrained("model/tokenizer")
session = ort.InferenceSession("model/model.onnx", providers=["CPUExecutionProvider"])

def embed_text(texts):
    if isinstance(texts, str):
        texts = [texts]

    inputs = tokenizer(texts, return_tensors="np", padding=True, truncation=True)
    ort_inputs = {
        "input_ids": inputs["input_ids"],
        "attention_mask": inputs["attention_mask"]
    }

    outputs = session.run(None, ort_inputs)
    embeddings = outputs[0][:, 0] 
    return np.array(embeddings)

def extract_keywords_from_text(text, top_k=10):
    keywords = set()
    try:
        yake_keywords = yake.KeywordExtractor(lan="en", n=1, top=top_k).extract_keywords(text)
        keywords.update([kw for kw, _ in yake_keywords])
    except Exception as e:
        print(f"[YAKE Error] {e}")
    return list(keywords)