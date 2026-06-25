# 🛡 Malicious Content Analysis using NLP

## 📌 Overview

This project presents an intelligent phishing email detection system based on Natural Language Processing (NLP) and Machine Learning.

The application compares two approaches:

- TF-IDF + Logistic Regression
- DistilBERT (Transformer-based model)

Users can:

- Paste email text directly
- Upload screenshots of emails (OCR with Tesseract)
- Compare predictions from both models
- Visualize phishing probabilities
- Read prevention recommendations

---

## 📂 Project Structure

malicious-content-analysis/
│
├── data/ # Final datasets used in the project
├── models/ # Trained ML models
├── UI/ # Streamlit application
├── results/ # Metrics, reports, confusion matrices, ROC curves
├── jupyter_lab/ # Training notebooks
└── README.md

---

## 📊 Dataset

The final datasets used for training and evaluation are available inside the `data/` folder.

Main files:

- `final_dataset.csv`
- `final_dataset2.csv`

The datasets were created by combining legitimate emails and phishing emails from multiple public sources.

They contain two classes:

- 0 → Legitimate email
- 1 → Phishing email

Researchers and students can directly download and reuse these files for educational or research purposes.

---

## 🤖 Models

### TF-IDF + Logistic Regression

Traditional NLP pipeline:

- Text preprocessing
- TF-IDF vectorization
- Logistic Regression classifier

Saved models:

- `models/tfidf_model.pkl`
- `models/logistic_model.pkl`

---

### DistilBERT

Modern transformer-based approach using Hugging Face Transformers.

Advantages:

- Contextual understanding
- Better semantic representations
- Higher robustness against sophisticated phishing attacks

Model files:

models/distilbert_model/

- config.json
- model.safetensors
- tokenizer.json
- tokenizer_config.json

---

## 📈 Experimental Results

Evaluation outputs are available inside the `results/` folder:

- metrics.txt
- classification_report.txt
- confusion_matrix.png
- roc_curve.png

The project achieved excellent performance on both approaches, with DistilBERT providing stronger contextual understanding while TF-IDF remains lightweight and fast.

---

## 🖥 Application Features

The Streamlit application allows users to:

### Text Analysis

- Paste an email
- Get predictions from both models
- Compare probabilities

### Image Analysis (OCR)

Users can upload:

- PNG
- JPG
- JPEG

The system extracts text using Tesseract OCR before performing classification.

### Security Recommendations

The application also provides phishing prevention advice, including:

- Never sharing passwords
- Verifying sender addresses
- Avoiding suspicious links
- Enabling two-factor authentication

---

## 🚀 Installation

Clone the repository:

git clone https://github.com/Tahacodeer/malicious-content-analysis.git

Install dependencies:

pip install -r requirements.txt

Launch the application:

streamlit run UI/app.py

---

## 👨‍💻 Authors

Developed as a university NLP project on malicious content detection using Machine Learning and Transformer models.

Team members:

- Taha lazhari
- hassan msaiaid


---

## 📜 License

This project is intended for educational and research purposes.
