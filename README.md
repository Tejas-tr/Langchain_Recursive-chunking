# ✂️ Recursive Text Chunking (RAG Building Block)

A small script demonstrating **recursive character text splitting** with LangChain — the process of breaking large documents into smaller, overlapping chunks before they're embedded and stored for retrieval in a RAG (Retrieval-Augmented Generation) pipeline.

---

## ✨ Features

- 🔀 **Recursive splitting strategy** — tries to split on paragraphs first, then falls back to sentences, then words, then characters, until each chunk fits within the target size.
- 📏 **Configurable chunk size** — control exactly how large each chunk can be (`chunk_size`).
- 🔗 **Chunk overlap** — preserves a few characters between consecutive chunks (`chunk_overlap`) so context isn't lost at chunk boundaries.
- 🪶 **Minimal, dependency-light example** — just LangChain's text splitter, no embedding model or vector store required to see the concept in action.

---

## 🗂️ Project Structure

```
.
└── Res_chunking.py   # Splits a markdown-style document into overlapping chunks
```

---

## 🛠️ Tech Stack

| Component                   | Purpose                                 |
|--------------------------------|--------------------------------------------|
| `langchain-text-splitters`      | Recursive character-based text splitting  |

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/recursive-text-chunking.git
cd recursive-text-chunking
```

### 2. Install dependencies
```bash
pip install langchain-text-splitters
```

### 3. Run the script
```bash
python Res_chunking.py
```

**Example output:**
```
12
['# Bengaluru Overview', '## Tech Industry', "Bengaluru is known as India's", ...]
```

The sample document (~500 characters covering Bengaluru's tech industry, climate, and food) gets split into small chunks of at most 40 characters each, with a 3-character overlap between consecutive chunks.

---

## 🧩 How It Works

`RecursiveCharacterTextSplitter` splits text using a prioritized list of separators — by default, in this order:

```
paragraph (\n\n) → sentence/line (\n) → word (space) → character
```

1. It first tries splitting the document on paragraph breaks.
2. If a resulting piece is still larger than `chunk_size`, it recursively splits that piece using the next separator down the list (sentences, then words, then raw characters).
3. This continues until every chunk fits within `chunk_size`.
4. `chunk_overlap` then stitches a small window of trailing characters from one chunk onto the start of the next — e.g. `['temperatu', 'atures']` share `'atu'` — so a sentence or idea split across a chunk boundary isn't completely lost from either side.

**Why this matters for RAG:**
Documents are almost always too large to embed and search as a single unit. Chunking breaks them into retrieval-sized pieces small enough to embed accurately and specific enough to return as relevant search results — while overlap helps prevent losing context right at the seams.

---

## 🔮 Roadmap

- [ ] Feed these chunks into a sentence-embedding model and store them in a vector database
- [ ] Compare `RecursiveCharacterTextSplitter` against other splitters (e.g. token-based, markdown-aware, semantic chunking)
- [ ] Experiment with different `chunk_size` / `chunk_overlap` values and measure retrieval quality
- [ ] Combine with the [cosine similarity project](#) to build a minimal end-to-end RAG retrieval pipeline

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

Built with [LangChain Text Splitters](https://python.langchain.com/docs/how_to/recursive_text_splitter/).
