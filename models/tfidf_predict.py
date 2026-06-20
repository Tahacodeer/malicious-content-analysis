import joblib

tfidf = joblib.load("models/tfidf_model.pkl")
model = joblib.load("models/logistic_model.pkl")


def predict_email(email):

    X = tfidf.transform([email])

    prediction = model.predict(X)[0]

    probability = model.predict_proba(X)[0]

    return {
        "prediction": int(prediction),
        "legitimate": float(probability[0]),
        "phishing": float(probability[1])
    }