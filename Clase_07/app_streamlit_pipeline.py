# App 2 · pipeline + Streamlit: el modelo corre en TU compu
import streamlit as st
from transformers import pipeline

MODELO = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"


@st.cache_resource
def cargar_pipe():
    return pipeline("text-classification", model=MODELO)


pipe = cargar_pipe()


def clasificar(texto):
    resultado = pipe(texto)[0]
    return f"{resultado['label']} ({resultado['score']:.1%})"


st.title("Clasificador (pipeline local)")
texto = st.text_input("Escribí una frase en inglés")

if texto:
    st.write(clasificar(texto))
