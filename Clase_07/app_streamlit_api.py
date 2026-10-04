# App 4 � InferenceClient + Streamlit: el modelo corre en el servidor de Hugging Face
import os
import streamlit as st
from huggingface_hub import InferenceClient

MODELO = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

@st.cache_resource
def crear_cliente():
    # Creamos el cliente con el proveedor y el token desde el entorno.
    return InferenceClient(
        provider="hf-inference",
        api_key=os.environ["HF_TOKEN"]
    )

client = crear_cliente()

st.title("Clasificador (Inference API)")
texto = st.text_input("Escrib� una frase")
if texto:
    # Consultamos el modelo remoto y mostramos etiqueta y puntaje.
    resultado = client.text_classification(texto, model=MODELO)
    st.write(f"{resultado[0].label} ({resultado[0].score:.1%})")
