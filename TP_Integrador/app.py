import os

import gradio as gr
from huggingface_hub import InferenceClient


MODELO = "MoritzLaurer/mDeBERTa-v3-base-mnli-xnli"

CATEGORIAS = [
    "problema de stock o producto faltante",
    "problema de precio o facturación",
    "problema de calidad del producto",
    "problema de atención al cliente",
    "problema de entrega o demora",
]


client = InferenceClient(
    provider="hf-inference",
    api_key=os.environ["HF_TOKEN"],
)


def clasificar_mensaje(texto):
    if not texto or not texto.strip():
        return (
            "Ingresá un mensaje para clasificar.",
            "",
            ""
        )

    resultado = client.zero_shot_classification(
        texto,
        candidate_labels=CATEGORIAS,
        model=MODELO,
        hypothesis_template="Este mensaje trata sobre {}.",
    )

    principal = resultado[0]

    ranking = "\n".join(
        f"{i}. {r.label} — {r.score:.1%}"
        for i, r in enumerate(resultado, start=1)
    )

    return (
        principal.label,
        f"{principal.score:.1%}",
        ranking,
    )


with gr.Blocks(title="Clasificador de mensajes de clientes") as demo:

    gr.Markdown(
        """
        # Clasificador de mensajes de clientes

        Clasifica mensajes breves según el motivo principal del contacto mediante
        **zero-shot classification** con un modelo multilingüe de Hugging Face.

        El sistema utiliza un modelo ya entrenado y no realiza entrenamiento adicional.
        """
    )

    with gr.Row():

        with gr.Column():
            texto = gr.Textbox(
                lines=6,
                label="Mensaje del cliente",
                placeholder="Ejemplo: Me cobraron dos veces el mismo producto.",
            )

            with gr.Row():
                boton_clasificar = gr.Button(
                    "Clasificar",
                    variant="primary"
                )
                boton_limpiar = gr.Button("Limpiar")

        with gr.Column():
            categoria = gr.Textbox(
                label="Categoría principal",
                interactive=False
            )

            confianza = gr.Textbox(
                label="Confianza",
                interactive=False
            )

            ranking = gr.Textbox(
                label="Ranking de categorías",
                lines=7,
                interactive=False
            )

    gr.Markdown(
        """
        ### Ejemplos

        - Me cobraron dos veces el mismo producto.
        - No había leche ni yogur en la góndola.
        - El pollo tenía mal olor cuando abrí el paquete.
        - La persona que me atendió resolvió mi problema muy rápido.
        - El pedido llegó dos horas tarde.

        ---
        **Nota:** la clasificación es automática y puede cometer errores,
        especialmente en mensajes ambiguos o que contengan más de un motivo.
        """
    )

    boton_clasificar.click(
        fn=clasificar_mensaje,
        inputs=texto,
        outputs=[
            categoria,
            confianza,
            ranking,
        ],
    )

    boton_limpiar.click(
        fn=lambda: ("", "", "", ""),
        inputs=[],
        outputs=[
            texto,
            categoria,
            confianza,
            ranking,
        ],
    )


if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860)),
    )