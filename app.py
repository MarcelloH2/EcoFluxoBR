import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-2.5-flash')

st.title("🌱 EcoFluxo - Dashboard de Triagem")

uploaded_file = st.file_uploader(
    "Capture ou envie uma foto do resíduo",
    type=['jpg', 'png', 'jpeg']
)

if uploaded_file:
    img = Image.open(uploaded_file)

    st.image(img, caption="Imagem do Sensor", width=400)

    if st.button("Analisar Material"):

        prompt = """
        Identifique se o objeto na foto é uma garrafa PET
        ou uma lata de alumínio.

        Responda apenas:
        'Material: [PET ou LATA]'

        seguido de uma breve explicação do porquê
        (brilho, forma ou transparência).
        """

        try:
            response = model.generate_content([prompt, img])

            st.subheader("Resultado da IA:")
            st.write(response.text)

        except Exception as e:
            st.error(f"Erro na API: {e}")