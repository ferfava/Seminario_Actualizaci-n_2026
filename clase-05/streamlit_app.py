"""Interfaz mínima equivalente para Streamlit Community Cloud."""

import streamlit as st

from logica import crear_saludo


st.set_page_config(page_title="Saludos · Clase 5", page_icon="👋")
st.title("Generador de saludos")
st.write("La misma lógica, ahora con Streamlit.")

with st.form("saludo"):
    nombre = st.text_input("Tu nombre")
    estilo = st.selectbox("Estilo del saludo", ["Amigable", "Formal", "Entusiasta"])
    enviar = st.form_submit_button("Crear saludo")

if enviar:
    st.success(crear_saludo(nombre, estilo))
