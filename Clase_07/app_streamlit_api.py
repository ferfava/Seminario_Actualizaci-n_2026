# App 4 · InferenceClient + Streamlit: el modelo corre en el servidor de Hugging Face
import os

import streamlit as st
from huggingface_hub import InferenceClient

MODELO = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"


@st.cache_resource
def crear_cliente():
    # Creamos el cliente con el proveedor y el token desde el entorno.
    return InferenceClient(
        provider="hf-inference",
        api_key=os.environ["HF_TOKEN"],
    )


client = crear_cliente()


def clasificar(texto):
    resultado = client.text_classification(texto, model=MODELO)
    return f"{resultado[0].label} ({resultado[0].score:.1%})"


st.title("Clasificador (Inference API)")
texto = st.text_input("Escribí una frase")

if texto:
    st.write(clasificar(texto))
