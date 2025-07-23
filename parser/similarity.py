from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from transformers import AutoTokenizer
import onnxruntime as ort

def compute_tfidf_similarity(texts):
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(texts)
    sim_matrix = cosine_similarity(tfidf_matrix)
    return sim_matrix

tokenizer = AutoTokenizer.from_pretrained("model/tokenizer")
session = ort.InferenceSession("model/model.onnx", providers=["CPUExecutionProvider"])

def compute_embedding_similarity(texts):
    if isinstance(texts, str):
        texts = [texts]
    inputs = tokenizer(texts, return_tensors="np", padding=True, truncation=True)
    ort_inputs = {
        "input_ids": inputs["input_ids"],
        "attention_mask": inputs["attention_mask"]
    }
    outputs = session.run(None, ort_inputs)
    embeddings = outputs[0][:, 0] 
    sim_matrix = cosine_similarity(embeddings)
    return sim_matrix

def pairwise_similarity(texts, use='tfidf'):
    if use == 'tfidf':
        return compute_tfidf_similarity(texts)
    elif use == 'minilm':
        return compute_embedding_similarity(texts)
    else:
        raise ValueError("Unsupported similarity type")