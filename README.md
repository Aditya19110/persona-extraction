# Persona-Driven Document Intelligence System

A sophisticated AI system that generates personalized reading paths from PDF documents based on user personas and cognitive profiles. Using advanced NLP techniques including MiniLM embeddings and Personalized PageRank algorithms, the system creates optimized document navigation tailored to individual user needs.

## Features

- **Persona-Driven Analysis**: Tailored document processing based on user cognitive profiles
- **Intelligent PDF Parsing**: Advanced section extraction with structure preservation
- **Semantic Graph Construction**: Build concept relationships using MiniLM embeddings
- **Personalized PageRank**: Custom ranking algorithm for relevance scoring
- **Dynamic Reading Paths**: Generate optimized reading sequences
- **Offline-First**: Complete local execution with ONNX-optimized models
- **Docker Support**: Containerized deployment for easy setup

## Architecture

```
PDFs → Section Extraction → Persona Profiling → Concept Graph → PageRank → Reading Path
```

1. **Section Extraction**: Parse PDFs and extract structured content
2. **Persona Profiling**: Build cognitive profiles from user characteristics
3. **Concept Graph**: Create semantic relationships between sections
4. **Personalized PageRank**: Rank content based on persona relevance
5. **Reading Path Generation**: Generate optimized reading sequences

## Prerequisites

- Python 3.8+
- Docker (optional, for containerized deployment)
- 4GB+ RAM recommended for large document processing

## Quick Start

### Option 1: Docker Deployment (Recommended)

```bash
# Build the Docker image
docker build -t persona-extractor .

# Run the container with data volume mounting
docker run --rm -v "$(pwd)/data:/app/data" persona-extractor
```

### Option 2: Local Installation

1. **Clone the repository**
```bash
git clone https://github.com/Aditya19110/persona-extraction
cd persona-extraction
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download SpaCy model** (if not already available)
```bash
python -m spacy download en_core_web_sm
```

5. **Run the system**
```bash
python main.py
```

## 📁 Project Structure

```
persona-extraction/
├── main.py                    # Main execution pipeline
├── config.py                  # Configuration settings
├── requirements.txt           # Python dependencies
├── Dockerfile                # Docker configuration
├── approach_explanation.md    # Detailed methodology
│
├── parser/
│   └── section_extractor.py  # PDF parsing and section extraction
│
├── nlp/
│   └── intent_model.py       # Persona profiling and intent extraction
│
├── graph/
│   ├── graph_builder.py      # Concept graph construction
│   ├── pagerank_traversal.py # Personalized PageRank implementation
│   └── reading_path_generator.py # Dynamic path generation
│
├── utils/
│   └── io_utils.py           # Input/output utilities
│
├── model/                    # Pre-downloaded models
│   ├── model.onnx           # ONNX-optimized MiniLM model
│   └── tokenizer/           # Local tokenizer files
│
└── data/                     # Data directory
    ├── input/               # Input PDF files
    ├── persona.json         # User persona configuration
    └── output/              # Generated results
```

## Configuration

Edit `config.py` to customize system behavior:

```python
PDF_INPUT_DIR = "data/input/"
PERSONA_JSON_PATH = "data/persona.json"
OUTPUT_JSON_PATH = "data/output/reading_path.json"

EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
ONNX_MODEL_PATH = "model/model.onnx"
TOKENIZER_PATH = "model/tokenizer/"

SIMILARITY_THRESHOLD = 0.2
MAX_READING_PATH_LENGTH = 10
PERSONALIZED_PAGERANK_ALPHA = 0.85
```

## Input Format

### Persona Configuration (`data/persona.json`)

```json
{
  "persona": "Senior Data Scientist",
  "job_to_be_done": "Understand machine learning deployment strategies for production systems",
  "depth": "deep",
  "style": "focused",
  "domain_expertise": "high",
  "time_constraint": "medium"
}
```

### Input Structure
```
data/
├── input/
│   ├── document1.pdf
│   ├── document2.pdf
│   └── ...
└── persona.json
```

## Output Format

The system generates a comprehensive JSON output:

```json
{
  "persona_profile": {
    "intent_keywords": ["machine learning", "deployment", "production"],
    "depth": "deep",
    "style": "focused"
  },
  "reading_path": [
    {
      "section_id": "doc1_section_3",
      "title": "ML Model Deployment Strategies",
      "summary": "Overview of deployment methodologies...",
      "relevance_score": 0.95,
      "source_document": "document1.pdf"
    }
  ],
  "metadata": {
    "total_sections_processed": 45,
    "processing_time": "2.3s",
    "similarity_method": "minilm"
  }
}
```

## Technical Stack

- **PDF Processing**: PyMuPDF
- **NLP**: SpaCy, KeyBERT, YAKE, Sumy
- **Embeddings**: MiniLM (all-MiniLM-L6-v2) via ONNX Runtime
- **Graph Processing**: NetworkX
- **Machine Learning**: scikit-learn, transformers
- **Optimization**: ONNX Runtime for fast inference

## Use Cases

- **Research Paper Navigation**: Quickly find relevant sections in academic papers
- **Technical Documentation**: Generate personalized reading paths for complex manuals
- **Legal Document Analysis**: Extract relevant clauses based on user needs
- **Educational Content**: Create customized learning paths from textbooks
- **Business Intelligence**: Personalized report analysis for executives

## Performance

- **Processing Speed**: ~2-5 seconds for 10-20 page documents
- **Memory Usage**: ~512MB-2GB depending on document size
- **Offline Operation**: Complete local execution with pre-downloaded models
- **Scalability**: Handles 100+ documents efficiently

## Models Included

**Pre-downloaded models are included in the repository:**
- MiniLM ONNX model (`model/model.onnx`)
- Tokenizer files (`model/tokenizer/`)
- No additional downloads required

## Algorithm Details

1. **Semantic Similarity**: Uses MiniLM embeddings for context-aware understanding
2. **Graph Construction**: Creates weighted edges based on content similarity
3. **Personalized PageRank**: Biases ranking toward persona-relevant content
4. **Path Optimization**: Generates coherent reading sequences


## Created By

Aditya Kulkarni & Vedika Lohiya