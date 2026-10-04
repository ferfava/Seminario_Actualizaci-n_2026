# App 3 � InferenceClient + Gradio: el modelo corre en el servidor de Hugging Face
import os
import gradio as gr
from huggingface_hub import InferenceClient

MODELO = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

# Creamos el cliente con el proveedor y el token desde el entorno.
client = InferenceClient(
    provider="hf-inference",
    api_key=os.environ["HF_TOKEN"]
)

def clasificar(texto):
    # Consultamos el modelo remoto y leemos los atributos del primer resultado.
    resultado = client.text_classification(texto, model=MODELO)
    return f"{resultado[0].label} ({resultado[0].score:.1%})"

demo = gr.Interface(fn=clasificar, inputs="text", outputs="text",
                    title="Clasificador (Inference API)")
demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))   # listo para Render
