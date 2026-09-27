"""Aplicación de ejemplo para la actividad de la clase 4."""

import os

import gradio as gr


def crear_saludo(nombre: str, estilo: str) -> str:
    """Devuelve un saludo según el estilo elegido."""
    nombre = nombre.strip()
    if not nombre:
        return "Escribí tu nombre para generar un saludo."

    saludos = {
        "Amigable": f"¡Hola, {nombre}! Qué bueno verte por acá.",
        "Formal": f"Buen día, {nombre}. Es un gusto saludarte.",
        "Entusiasta": f"¡Bienvenido/a, {nombre}! ¡Vamos con todo!",
    }
    return saludos.get(estilo, saludos["Amigable"])


with gr.Blocks(title="Saludos · Clase 4") as demo:
    gr.Markdown("# Generador de saludos\nUna app de ejemplo hecha con Gradio Blocks.")
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
    # El enlace temporal se genera desde la computadora local. En Spaces,
    # Hugging Face publica la aplicación y no hace falta un túnel de Gradio.
    demo.launch(share=os.getenv("SPACE_ID") is None)
