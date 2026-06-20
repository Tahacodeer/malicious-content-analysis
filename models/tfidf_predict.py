import joblib

model = joblib.load("models/logistic_model.pkl")
tfidf = joblib.load("models/tfidf_model.pkl")


def predict_email(email):

    x = tfidf.transform([email])

    proba = model.predict_proba(x)[0]

    return {
        "prediction": int(proba[1] >= 0.445),
        "legitimate": float(proba[0]),
        "phishing": float(proba[1])
    }