# 🧠 Persona-Driven Document Intelligence System – Approach Explanation

## 1. Objective

Our system generates a **personalized, ranked reading path** from a collection of PDF documents, tailored to a specific persona's cognitive profile and their job-to-be-done. The goal is to create an intelligent document navigation system that understands both content semantics and user intent to deliver the most relevant information in an optimal sequence.

## 2. Core Methodology

### 2.1 PDF Parsing & Section Extraction
- **Technology**: PyMuPDF for robust PDF text extraction
- **Process**: Extract text sections while preserving document structure
- **Features**: Capture layout information (font sizes, positioning) to identify headings, paragraphs, and content hierarchy
- **Output**: Structured sections with metadata for downstream processing

### 2.2 Persona Cognitive Profiling
- **Input**: `persona.json` containing user characteristics and objectives
- **Intent Extraction**: Hybrid keyword extraction using:
  - **YAKE**: Statistical keyword extraction for domain-specific terms
  - **KeyBERT**: Transformer-based keyword extraction using local ONNX model
- **Profile Construction**: Generate intent keywords and classify reading preferences:
  - **Depth**: "deep" (comprehensive) vs "shallow" (overview)
  - **Style**: "focused" (targeted) vs "exploratory" (broad)

### 2.3 Concept Graph Construction
- **Graph Structure**: 
  - **Nodes**: Document sections with embedded content
  - **Edges**: Semantic similarity relationships
- **Similarity Computation**: 
  - **Option 1**: TF-IDF vectorization with cosine similarity
  - **Option 2**: MiniLM embeddings (`all-MiniLM-L6-v2`) for semantic understanding
- **Edge Filtering**: Apply configurable similarity threshold to create meaningful connections
- **Output**: Weighted graph representing document concept relationships

### 2.4 Personalized PageRank Algorithm
- **Personalization Vector**: Constructed from persona intent keywords
- **Algorithm**: Modified PageRank with persona-specific node biasing
- **Parameters**: 
  - Alpha = 0.85 (damping factor)
  - Personalization based on keyword-section relevance
- **Result**: Ranked nodes reflecting persona-specific importance scores

### 2.5 Dynamic Reading Path Generation
- **Selection**: Choose top-k sections based on PageRank scores
- **Summarization**: Apply extractive summarization (TextRank/LexRank/Sumy)
- **Path Optimization**: Order sections for logical reading flow
- **Output Structure**:
  ```json
  {
    "persona_profile": {...},
    "reading_path": [
      {
        "section_id": "...",
        "title": "...",
        "summary": "...",
        "relevance_score": 0.95,
        "source_document": "..."
      }
    ],
    "metadata": {...}
  }
  ```

## 3. Offline-First Architecture

### 3.1 Local Model Infrastructure
- **MiniLM Model**: ONNX-optimized version stored in `model/model.onnx`
- **Tokenizer**: Local tokenizer files in `model/tokenizer/`
- **No Internet Dependency**: Complete offline execution capability

### 3.2 Performance Optimizations
- **ONNX Runtime**: Fast inference for embedding generation
- **Caching**: Efficient similarity computation and storage
- **Memory Management**: Optimized for large document collections

### 3.3 Fallback Mechanisms
- **TF-IDF Backup**: Alternative similarity measure if MiniLM fails
- **Robust Error Handling**: Graceful degradation for edge cases

## 4. Technical Stack

### 4.1 Core Dependencies
- **PyMuPDF**: PDF parsing and text extraction
- **NetworkX**: Graph construction and PageRank implementation
- **scikit-learn**: TF-IDF vectorization and ML utilities
- **ONNX Runtime**: Fast local model inference
- **sentence-transformers**: MiniLM model integration

### 4.2 NLP Pipeline
- **SpaCy**: Text preprocessing and tokenization
- **KeyBERT + YAKE**: Hybrid keyword extraction
- **Sumy**: Extractive text summarization

## 5. Innovation Highlights

### 5.1 Semantic Understanding
- **Context-Aware**: MiniLM embeddings capture semantic meaning beyond keyword matching
- **Relationship Modeling**: Graph structure represents inter-section dependencies

### 5.2 Personalization Engine
- **Multi-Dimensional Profiling**: Considers intent, depth, and style preferences
- **Adaptive Ranking**: PageRank algorithm tailored to individual user profiles

### 5.3 Scalable Architecture
- **Modular Design**: Loosely coupled components for easy extension
- **Configuration-Driven**: Tunable parameters for different use cases
- **Production-Ready**: ONNX optimization for deployment efficiency

## 6. Evaluation Metrics

- **Relevance Accuracy**: Alignment with persona objectives
- **Coverage Completeness**: Important information inclusion
- **Reading Efficiency**: Optimal information density
- **Execution Performance**: Processing speed and memory usage

## 7. Future Extensions

- **Multi-Modal Support**: Images, tables, and charts processing
- **Interactive Refinement**: User feedback integration
- **Domain Adaptation**: Specialized models for specific fields
- **Real-Time Updates**: Dynamic path adjustment based on reading progress

---

This approach combines cutting-edge NLP techniques with classical graph algorithms to deliver a sophisticated, personalized document intelligence system that operates entirely offline while maintaining high performance and accuracy.