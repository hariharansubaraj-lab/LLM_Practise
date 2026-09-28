# LLM Practice: Tokenization, Prompt Engineering & Local LLM API

This repository contains practical implementations and experiments with Large Language Models (LLMs), covering tokenization, prompt engineering methodologies, and building a local LLM API with FastAPI and Ollama.

---

## 📂 Project Structure

```
LLM_Pratice/
├── requirements.txt
├── README.md
├── tokenization/
│   └── tokenizer_demo.py          # HuggingFace tokenization demo
├── llm/
│   └── llm_client.py              # Ollama API client (llama3.2)
├── prompt_engineering/
│   └── prompts.py                 # 10 prompt engineering strategies
└── api/
    └── main.py                    # FastAPI service exposing LLM endpoints
```

---

## 🚀 Key Modules

### 1. Tokenization (`tokenization/tokenizer_demo.py`)
- Uses Hugging Face's `transformers` library with `bert-base-uncased`.
- Demonstrates converting raw text into tokens, mapping tokens to IDs, and calculating total token counts.

### 2. Ollama Client (`llm/llm_client.py`)
- Connects directly to local Ollama instance (`http://localhost:11434/api/generate`).
- Configured for `llama3.2` model inference with synchronous response extraction.

### 3. Prompt Engineering (`prompt_engineering/prompts.py`)
Comprehensive evaluation of 10 distinct prompt engineering strategies for sentiment classification:
1. **Zero-shot**: Basic instruction.
2. **Clear Zero-shot**: Explicit constraint on returning only the classification.
3. **Role-based Prompt**: Assigning a persona/system identity.
4. **Structured Prompt**: Formatted with clear task, review, and allowed labels.
5. **One-shot**: Single exemplar demonstration.
6. **Few-shot**: Multiple exemplars covering positive and negative cases.
7. **Few-shot Structured**: Structured format with multiple exemplars.
8. **Reasoning-style**: Instructing the model to evaluate nuances before answering.
9. **Step-by-step Reasoning**: Chain-of-thought breakdown of features before determining sentiment.
10. **Production-style Prompt**: Strict constraints, rules, and deterministic output formatting.

### 4. FastAPI Service (`api/main.py`)
- Exposes RESTful endpoints using FastAPI:
  - `GET /`: Health check endpoint.
  - `POST /ask`: Accepts prompt input and returns model response from the local Ollama LLM.

---

## 🛠️ Setup & Installation

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Prerequisites: Ollama

Ensure Ollama is installed and running with `llama3.2`:

```bash
ollama run llama3.2
```

---

## 🧪 Running the Code

### Run Tokenizer Demo
```bash
python tokenization/tokenizer_demo.py
```

### Run Prompt Engineering Experiments
```bash
python prompt_engineering/prompts.py
```

### Start FastAPI Server
```bash
uvicorn api.main:app --reload --port 8000
```

Access Swagger docs at: `http://localhost:8000/docs`
