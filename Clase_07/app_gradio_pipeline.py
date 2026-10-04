# App 1 · pipeline + Gradio: el modelo corre en TU compu
import gradio as gr
from transformers import pipeline

MODELO = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
pipe = pipeline("text-classification", model=MODELO)   # afuera: se carga una vez

def clasificar(texto):
    resultado = pipe(texto)[0]
    return f"{resultado['label']} ({resultado['score']:.1%})"


demo = gr.Interface(fn=clasificar, inputs="text", outputs="text",
                    title="Clasificador (pipeline local)")
demo.launch()
