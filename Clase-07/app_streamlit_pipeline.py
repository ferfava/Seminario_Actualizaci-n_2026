# App 2 � pipeline + Streamlit: el modelo corre en TU compu
import streamlit as st
from transformers import pipeline

MODELO = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

@st.cache_resource
def cargar_pipe():
    return pipeline("text-classification", model=MODELO)


pipe = cargar_pipe()

st.title("Clasificador (pipeline local)")
texto = st.text_input("Escrib� una frase en ingl�s")

if texto:
    resultado = pipe(texto)[0]
    st.write(f"{resultado['label']} ({resultado['score']:.1%})")
