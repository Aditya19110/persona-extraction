# === General Paths ===
PDF_INPUT_DIR = "data/input_pdfs/"
PERSONA_JSON_PATH = "data/persona.json"
OUTPUT_JSON_PATH = "data/output.json"

# === Section Extraction ===
HEADING_FONT_THRESHOLD = 13  # Font size to consider something a heading

# === Graph Construction ===
SIMILARITY_MEASURE = "minilm"  # Only use local minilm
SIMILARITY_THRESHOLD = 0.2     # For graph edge creation

# === PageRank & Traversal ===
MAX_READING_PATH_LENGTH = 10
PERSONALIZED_PAGERANK_ALPHA = 0.85

# === Summarization ===
SUMMARY_SENTENCES = 2

# === Keyword Extraction ===
NUM_KEYWORDS = 10

# === Embedding Model (Local Only) ===
ONNX_MODEL_PATH = "model/model.onnx"
TOKENIZER_PATH = "model/tokenizer"

# === Runtime Constraints ===
MAX_MEMORY_MB = 1024
CPU_ONLY = True
OFFLINE_MODE = True