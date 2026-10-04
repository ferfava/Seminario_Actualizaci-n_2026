# TP Integrador — Clasificador de mensajes de clientes

**Fernanda Andrea Fava**  
Seminario de Actualización · IFTS N.º 18 · 2026

## Problema

El objetivo es clasificar mensajes breves de clientes según el motivo principal del contacto.

Las categorías utilizadas son:

- problema de stock o producto faltante
- problema de precio o facturación
- problema de calidad del producto
- problema de atención al cliente
- problema de entrega o demora

## Enfoque

La solución utiliza **zero-shot classification**, por lo que no fue necesario entrenar un modelo propio.

Se compararon dos modelos multilingües preentrenados de Hugging Face:

- `MoritzLaurer/multilingual-MiniLMv2-L6-mnli-xnli`
- `MoritzLaurer/mDeBERTa-v3-base-mnli-xnli`

Ambos fueron evaluados con `pipeline` e `InferenceClient` utilizando los mismos mensajes y categorías.

## Resultados

| Modelo | Método | Accuracy |
|---|---|---:|
| MiniLM | pipeline | 50 % |
| MiniLM | InferenceClient | 50 % |
| mDeBERTa | pipeline | 87,5 % |
| mDeBERTa | InferenceClient | 87,5 % |

Se seleccionó **mDeBERTa** por su mejor desempeño en el conjunto de prueba.

## Modelo final

`MoritzLaurer/mDeBERTa-v3-base-mnli-xnli`

La aplicación utiliza `InferenceClient`, por lo que el modelo se ejecuta en la infraestructura del proveedor y no en el servidor donde vive la interfaz.

Esto permite publicar la aplicación sin descargar los pesos del modelo ni instalar `torch` en el entorno de despliegue.

## Aplicación

La interfaz fue desarrollada con **Gradio**.

Archivo principal:

`app.py`

## Ejecución local

Crear un entorno virtual:

```powershell
python -m venv .venv