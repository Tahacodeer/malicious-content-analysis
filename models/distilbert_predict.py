import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

MODEL_PATH = "models/distilbert_model"

tokenizer = DistilBertTokenizer.from_pretrained(MODEL_PATH)

model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)

model.eval()

def predict_email(text):

    inputs = tokenizer(
        text,
        truncation=True,
        padding=True,
        max_length=256,
        return_tensors="pt"
    )

    with torch.no_grad():
        outputs = model(**inputs)

    probs = torch.softmax(outputs.logits, dim=1)

    prediction = torch.argmax(probs, dim=1).item()

    return {
        "prediction": prediction,
        "legitimate": float(probs[0][0]),
        "phishing": float(probs[0][1])
    }