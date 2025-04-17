# 🧠 LexMatch 
### Semantic Similarity Engine (Cosine-Based)

This project implements a simple semantic similarity engine in Python. It uses **cosine similarity** to compare word meaning based on **co-occurrence patterns** in text. You can use it to evaluate how similar different words are based on the contexts they appear in.

> ⚠️ **Note**: This repo includes only the code. You'll need to supply your own text corpora and test files to run the full similarity evaluation.

---

## 📌 What It Does

- Builds **semantic descriptors** (co-occurrence vectors) for words using sentences from text.
- Computes **cosine similarity** between word vectors.
- Answers multiple-choice word similarity questions by selecting the most semantically related option.
- Outputs an **accuracy score** based on how often it selects the correct choice.

---

## 🧠 Key Components

| Function | Description |
|----------|-------------|
| `cosine_similarity()` | Computes cosine similarity between two word vectors |
| `build_semantic_descriptors()` | Builds co-occurrence vectors from sentences |
| `build_semantic_descriptors_from_files()` | Parses files and builds descriptors from raw text |
| `most_similar_word()` | Chooses the closest matching word based on similarity |
| `run_similarity_test()` | Evaluates model performance on a test set |

---

## 🛠 Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/semantic-similarity-engine.git
   cd semantic-similarity-engine
   ```

2. Supply your own text files:
   - `wp.txt`, `sw.txt`: Any large text corpus (e.g., Wikipedia dumps, novels, etc.)
   - `test.txt`: A test file in the format:
     ```
     word correct_choice option1 option2 ...
     ```

3. Run the script:
   ```bash
   python3 main.py
   ```

4. Output will look like:
   ```
   72.5 of the guesses were correct
   ```

---

## 🔍 Example (for your own testing)

Given a line in `test.txt`:
```
bright shiny dull light dark
```

The script will:
- Compare the word "bright" with each of the choices.
- Select the one most similar based on semantic context learned from your training files.

---

## 🧠 Why It's Cool

- Implements the foundations of **distributional semantics**.
- Lightweight and interpretable — no external ML libraries required.
- Easy to extend with other similarity functions or vector-building strategies.

---

## 📁 Included

- `main.py` — the full working semantic similarity engine

📄 No datasets are included. To test this script, please supply your own `.txt` files.


Built with <3 by Manroop Kalsi
