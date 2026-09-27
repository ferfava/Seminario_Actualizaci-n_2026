"""Lógica compartida por las interfaces Gradio y Streamlit."""


def crear_saludo(nombre: str, estilo: str) -> str:
    nombre = nombre.strip()
    if not nombre:
        return "Escribí tu nombre para generar un saludo."

    saludos = {
        "Amigable": f"¡Hola, {nombre}! Qué bueno verte por acá.",
        "Formal": f"Buen día, {nombre}. Es un gusto saludarte.",
        "Entusiasta": f"¡Bienvenido/a, {nombre}! ¡Vamos con todo!",
    }
    return saludos.get(estilo, saludos["Amigable"])
