# nlp/keyword_extractor.py

import yake
import numpy as np
from transformers import AutoTokenizer
import onnxruntime as ort
import json

# === Load local tokenizer ===
tokenizer = AutoTokenizer.from_pretrained("model/tokenizer")

# === Load ONNX model ===
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
    embeddings = outputs[0][:, 0]  # CLS token
    return np.array(embeddings)

def extract_keywords_from_text(text, top_k=10):
    keywords = set()

    # === YAKE ===
    try:
        yake_keywords = yake.KeywordExtractor(lan="en", n=1, top=top_k).extract_keywords(text)
        keywords.update([kw for kw, _ in yake_keywords])
    except Exception as e:
        print(f"[YAKE Error] {e}")

    # === Embedding similarity scoring (optional, if needed later) ===
    # You can score the keywords by embedding them and comparing to the doc embedding

    return list(keywords)