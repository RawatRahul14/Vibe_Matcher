# Vibe Matcher

Vibe Matcher is a semantic fashion recommendation prototype that matches a user's "vibe query" (like *"energetic urban chic"*) to the most relevant products in a catalog using OpenAI embeddings and cosine similarity.

This system demonstrates how AI understanding of language can power personalized recommendations - connecting style intent to actual products.

---

## Overview

The goal was to build a **mini recommendation engine** capable of:

1. Accepting a **vibe-style query**.
2. Embedding product descriptions + user query using OpenAI
3. Comparing embeddings using cosine similarity (sklearn)
4. Returning top-3 matches with similarity scores
5. Logging query performance and latency

---

## Features

### Data Pipeline

* Mock fashion dataset (10 items)
* Incremental embedding updates (avoids re-embedding)
* Separate folders for raw and embedded data

### Embedding Engine

* Uses `text-embedding-ada-002`
* Tracks latency and token count
* Handles retry and exception safety

### Matching Engine

* Cosine similarity with sklearn
* Threshold filtering (>= 0.7)
* Returns Top-3 sorted matches
* Human-readable fallback if no strong matches

### Evaluation & Logging

* Logs to:

  * `logs/data_pipeline.log`
  * `logs/embedding_pipeline.log`
  * `logs/matching_pipeline.log`
* Query performance in `logs/query_eval_log.csv`
* Visualization of latency using matplotlib

---

## Architecture

```
Vibe_Matcher/
│
├── data/
│   ├── raw/                (Base dataset)
│   └── embeddings/         (Vectorized dataset)
│
├── logs/
│   ├── data_pipeline.log
│   ├── embedding_pipeline.log
│   ├── matching_pipeline.log
│   └── query_eval_log.csv
│
├── utils/
│   ├── __init__.py         (Logger setup)
│
├── notebooks/
│   └── vibe_matcher_notebook.ipynb (Main workflow)
│
├── requirements.txt
└── README.md
```

---

## Example Results

| Query                   | Top-3 Recommendations                       | Avg Similarity | Status    |
| :---------------------- | :------------------------------------------ | :------------- | :-------- |
| energetic urban chic    | Street Hoodie, Athleisure Set, Boho Dress   | 0.83           | ✅ Success |
| cozy winter comfort     | Cozy Sweater, Athleisure Set, Street Hoodie | 0.84           | ✅ Success |
| luxury evening glamour  | Silk Gown, Festival Kimono, Boho Dress      | 0.84           | ✅ Success |
| techwear cyberpunk neon | Festival Kimono, Street Hoodie, Chic Blazer | 0.80           | ✅ Success |

---

## Evaluation

All queries logged in `logs/query_eval_log.csv`.
Use the visualization function:

```python
plot_query_latency()
```

Generates a bar chart of query vs latency with annotations and average latency title.

---

## Reflection

✅ Modular pipelines for data, embeddings, and matching  
✅ Latency + similarity metrics logged and visualized  
✅ Handled edge cases (empty embeddings, weak matches)

**Future Improvements:**

* Add Pinecone or FAISS for large-scale vector search
* Deploy FastAPI endpoints for real-time matching
* Add image embeddings for multi-modal matching
* Introduce user feedback learning loop

---

## Tech Stack

| Category      | Tools                         |
| :------------ | :---------------------------- |
| Embeddings    | OpenAI text-embedding-ada-002 |
| Similarity    | sklearn cosine_similarity     |
| Logging       | Python logging                |
| Data          | pandas, numpy                 |
| Visualization | matplotlib                    |
| Env           | dotenv, Python 3.11+          |

---

## Running the Project

```bash
# 1. Clone the repo
git clone https://github.com/RawatRahul14/Vibe_Matcher.git
cd Vibe_Matcher

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set API key
echo "OPENAI_API_KEY=your_key_here" > .env
```

---