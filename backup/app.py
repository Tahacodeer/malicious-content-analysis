import streamlit as st
import pytesseract

from PIL import Image

import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from models.tfidf_predict import predict_email

st.set_page_config(
    page_title="Détection de Phishing",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Détection d’E-mails de Phishing")

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

            result = predict_email(email_text)

            phishing = result["phishing"]
            legit = result["legitimate"]

            if result["prediction"] == 1:

                st.error("⚠️ E-mail potentiellement malveillant")

            else:

                st.success("✅ E-mail légitime")

            st.progress(float(phishing))

            st.metric(
                "Probabilité de phishing",
                f"{phishing*100:.2f}%"
            )

            st.metric(
                "Probabilité légitime",
                f"{legit*100:.2f}%"
            )

# ===================================================
# IMAGE TAB
# ===================================================

with tab2:

    st.subheader("Analyser une capture d’écran")

    uploaded_file = st.file_uploader(
        "Importer une image",
        type=["png","jpg","jpeg"]
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Image importée",
            use_container_width=True
        )

        extracted_text = pytesseract.image_to_string(
            image
        )

        st.text_area(
            "Texte extrait",
            extracted_text,
            height=250
        )

        if st.button("Analyser l’image"):

            result = predict_email(
                extracted_text
            )

            phishing = result["phishing"]
            legit = result["legitimate"]

            if result["prediction"] == 1:

                st.error(
                    "⚠️ E-mail potentiellement malveillant"
                )

            else:

                st.success(
                    "✅ E-mail légitime"
                )

            st.progress(float(phishing))

            st.metric(
                "Probabilité de phishing",
                f"{phishing*100:.2f}%"
            )

            st.metric(
                "Probabilité légitime",
                f"{legit*100:.2f}%"
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