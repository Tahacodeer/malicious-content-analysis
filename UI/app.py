import streamlit as st
import pytesseract
from PIL import Image

import sys
import os

ROOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from models.tfidf_predict import predict_email as tfidf_predict

# ==========================
# Chargement DistilBERT
# ==========================

DISTILBERT_AVAILABLE = True
DISTILBERT_ERROR = ""


DISTILBERT_AVAILABLE = True
DISTILBERT_ERROR = ""

try:
    from models.distilbert_predict import predict_email as distilbert_predict
except Exception as e:
    DISTILBERT_AVAILABLE = False
    DISTILBERT_ERROR = str(e)
st.set_page_config(
    page_title="Détection de Phishing",
    page_icon="🛡",
    layout="wide"
)

st.title("🛡 Détection d’E-mails de Phishing")

st.markdown("""
Analyse automatique d’e-mails suspects à l’aide du NLP et du Machine Learning.
""")

tab1, tab2 = st.tabs(
    ["✍️ Texte", "📷 Image"]
)

# ===================================================
# TEXT TAB
# ===================================================

with tab1:

    st.subheader("Analyser un e-mail")

    email_text = st.text_area(
        "Collez le contenu de l’e-mail :",
        height=250
    )

    if st.button("Analyser le texte"):

        if email_text.strip() != "":

            tfidf_result = tfidf_predict(email_text)

            if DISTILBERT_AVAILABLE:
                distilbert_result = distilbert_predict(email_text)

            col1, col2 = st.columns(2)

            # ==========================
            # TF-IDF
            # ==========================

            with col1:

                st.subheader("TF-IDF + Logistic Regression")

                if tfidf_result["prediction"] == 1:
                    st.error("⚠️ Phishing")
                else:
                    st.success("✅ Légitime")

                st.progress(float(tfidf_result["phishing"]))

                st.metric(
                    "Probabilité de phishing",
                    f"{tfidf_result['phishing']*100:.2f}%"
                )

                st.metric(
                    "Probabilité légitime",
                    f"{tfidf_result['legitimate']*100:.2f}%"
                )

            # ==========================
            # DistilBERT
            # ==========================

            with col2:

                st.subheader("DistilBERT")

                if not DISTILBERT_AVAILABLE:

                    st.warning("⚠️ Modèle DistilBERT indisponible")
                    st.code(DISTILBERT_ERROR)

                else:

                    if distilbert_result["prediction"] == 1:
                        st.error("⚠️ Phishing")
                    else:
                        st.success("✅ Légitime")

                    st.progress(float(distilbert_result["phishing"]))

                    st.metric(
                        "Probabilité de phishing",
                        f"{distilbert_result['phishing']*100:.2f}%"
                    )

                    st.metric(
                        "Probabilité légitime",
                        f"{distilbert_result['legitimate']*100:.2f}%"
                    )

# ===================================================
# IMAGE TAB
# ===================================================

with tab2:

    st.subheader("Analyser une capture d’écran")

    uploaded_file = st.file_uploader(
        "Importer une image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Image importée",
            use_container_width=True
        )

        extracted_text = pytesseract.image_to_string(image)

        st.text_area(
            "Texte extrait",
            extracted_text,
            height=250
        )

        if st.button("Analyser l’image"):

            tfidf_result = tfidf_predict(extracted_text)

            if DISTILBERT_AVAILABLE:
                distilbert_result = distilbert_predict(extracted_text)

            col1, col2 = st.columns(2)

            # ==========================
            # TF-IDF
            # ==========================

            with col1:

                st.subheader("TF-IDF + Logistic Regression")

                if tfidf_result["prediction"] == 1:
                    st.error("⚠️ Phishing")
                else:
                    st.success("✅ Légitime")

                st.progress(float(tfidf_result["phishing"]))

                st.metric(
                    "Probabilité de phishing",
                    f"{tfidf_result['phishing']*100:.2f}%"
                )

                st.metric(
                    "Probabilité légitime",
                    f"{tfidf_result['legitimate']*100:.2f}%"
                )

            # ==========================
            # DistilBERT
            # ==========================

            with col2:

                st.subheader("DistilBERT")

                if not DISTILBERT_AVAILABLE:

                    st.warning("⚠️ Modèle DistilBERT indisponible")
                    st.code(DISTILBERT_ERROR)

                else:

                    if distilbert_result["prediction"] == 1:
                        st.error("⚠️ Phishing")
                    else:
                        st.success("✅ Légitime")

                    st.progress(float(distilbert_result["phishing"]))

                    st.metric(
                        "Probabilité de phishing",
                        f"{distilbert_result['phishing']*100:.2f}%"
                    )

                    st.metric(
                        "Probabilité légitime",
                        f"{distilbert_result['legitimate']*100:.2f}%"
                    )

# ===================================================
# PREVENTION
# ===================================================

st.divider()

st.subheader("🔐 Conseils de prévention")

st.info("""
• Ne jamais partager vos mots de passe.

• Vérifier l’adresse de l’expéditeur.

• Éviter de cliquer sur des liens suspects.

• Vérifier les fautes d’orthographe.

• Activer l’authentification à deux facteurs.
""")