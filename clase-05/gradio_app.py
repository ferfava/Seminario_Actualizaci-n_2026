"""Interfaz Gradio Blocks para desplegar en Render."""

import os

import gradio as gr

from logica import crear_saludo


with gr.Blocks(title="Saludos · Clase 5") as demo:
    gr.Markdown("# Generador de saludos\nLa misma lógica con Gradio Blocks.")
    with gr.Row():
        nombre = gr.Textbox(label="Tu nombre", placeholder="Escribí tu nombre")
        estilo = gr.Dropdown(
            choices=["Amigable", "Formal", "Entusiasta"],
            value="Amigable",
            label="Estilo del saludo",
        )
    boton = gr.Button("Crear saludo", variant="primary")
    resultado = gr.Textbox(label="Resultado", interactive=False)
    boton.click(fn=crear_saludo, inputs=[nombre, estilo], outputs=resultado)


if __name__ == "__main__":
    # Render inyecta PORT; el servidor debe escuchar en todas las interfaces.
    puerto = os.environ.get("PORT")
    demo.launch(
        server_name="0.0.0.0" if puerto else "127.0.0.1",
        server_port=int(puerto) if puerto else 7860,
        share=False,
    )
