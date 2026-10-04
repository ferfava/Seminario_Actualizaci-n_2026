# TP Integrador — Clasificador de mensajes de clientes

**Fernanda Andrea Fava**  
Seminario de Actualización · IFTS N.º 18 · 2026

## Descripción

Este trabajo práctico desarrolla una aplicación capaz de **clasificar mensajes breves de clientes según el motivo principal del contacto** utilizando un modelo de lenguaje ya entrenado disponible en Hugging Face.

El proyecto utiliza **zero-shot classification**: no se entrenó un modelo propio. En su lugar, se compararon modelos preentrenados y se seleccionó el que ofreció mejor desempeño para mensajes breves en español.

## Problema

El objetivo es asignar cada mensaje a una categoría principal entre las siguientes:

- problema de stock o producto faltante
- problema de precio o facturación
- problema de calidad del producto
- problema de atención al cliente
- problema de entrega o demora

La aplicación está pensada como una demostración de cómo un sistema de IA puede ayudar a organizar automáticamente consultas o reclamos de clientes.

## Modelos evaluados

Se compararon dos modelos multilingües de Hugging Face para zero-shot classification:

1. `MoritzLaurer/multilingual-MiniLMv2-L6-mnli-xnli`
2. `MoritzLaurer/mDeBERTa-v3-base-mnli-xnli`

Ambos se evaluaron con:

- `transformers.pipeline`
- `huggingface_hub.InferenceClient`

Para mantener una comparación consistente, se utilizaron los mismos mensajes de prueba, las mismas categorías y la misma plantilla de hipótesis:

```text
Este mensaje trata sobre {}.
```

## Resultados

| Modelo | Método | Aciertos | Total | Accuracy | Tiempo promedio (s) |
|---|---|---:|---:|---:|---:|
| MiniLM | pipeline | 4 | 8 | 50 % | 0,033 |
| MiniLM | InferenceClient | 4 | 8 | 50 % | 0,908 |
| mDeBERTa | pipeline | 7 | 8 | 87,5 % | 2,067 |
| mDeBERTa | InferenceClient | 7 | 8 | 87,5 % | 1,021 |

Los resultados muestran que, en este conjunto de prueba, **la elección del modelo tuvo mayor impacto sobre la calidad de clasificación que el método utilizado para ejecutar la inferencia**.

Los tiempos corresponden a estas ejecuciones concretas y pueden variar por hardware, latencia de red o inicialización del servicio.

## Modelo seleccionado

El modelo elegido para la aplicación final es:

`MoritzLaurer/mDeBERTa-v3-base-mnli-xnli`

Se seleccionó porque obtuvo **7 aciertos sobre 8 casos (87,5 %)**, frente al 50 % obtenido por MiniLM.

## Estrategia de inferencia

La aplicación final utiliza **`InferenceClient`**.

Esta decisión permite usar mDeBERTa sin cargar localmente sus pesos en el servidor de la interfaz. La aplicación envía el mensaje al proveedor de inferencia y recibe el resultado de la clasificación.

Esto reduce los requisitos del entorno de despliegue y evita instalar `torch` y descargar el modelo completo en el servidor donde se publica la interfaz.

## Arquitectura

```text
Usuario
   ↓
Interfaz Gradio
   ↓
app.py
   ↓
InferenceClient
   ↓
Proveedor de inferencia de Hugging Face
   ↓
mDeBERTa
   ↓
Resultado de clasificación
   ↓
Interfaz Gradio
```

### ¿Dónde vive cada componente?

- **Interfaz:** Gradio.
- **Código de la aplicación:** `app.py`.
- **Modelo:** Hugging Face Hub.
- **Inferencia final:** remota mediante `InferenceClient`.
- **Análisis y comparación de modelos:** `TP_Fava_Fernanda.ipynb`.

## Funcionalidades de la aplicación

La interfaz permite:

- ingresar un mensaje breve de un cliente;
- obtener la categoría principal;
- visualizar el nivel de confianza;
- consultar el ranking completo de categorías;
- limpiar los resultados y realizar una nueva consulta.

La interfaz está desarrollada completamente en español.

## Estructura del proyecto

```text
TP_Integrador/
│
├── app.py
├── requirements.txt
├── README.md
└── TP_Fava_Fernanda.ipynb
```

El informe en PDF y la presentación final se incorporarán como parte de la entrega final.

## Requisitos

Para ejecutar la aplicación localmente se necesita:

- Python 3
- conexión a internet
- cuenta de Hugging Face
- token de Hugging Face válido para utilizar el proveedor de inferencia

## Instalación local

### 1. Clonar el repositorio

```powershell
git clone https://github.com/ferfava/Seminario_Actualizacion_2026.git
```

### 2. Entrar a la carpeta del proyecto

```powershell
cd Seminario_Actualizacion_2026\TP_Integrador
```

### 3. Crear un entorno virtual

```powershell
python -m venv .venv
```

### 4. Activarlo en Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Instalar las dependencias

```powershell
python -m pip install -r requirements.txt
```

## Configuración del token de Hugging Face

El token **no debe escribirse dentro del código ni subirse al repositorio**.

En PowerShell puede cargarse temporalmente mediante:

```powershell
$env:HF_TOKEN = Read-Host "Token de Hugging Face"
```

La aplicación obtiene el token desde la variable de entorno `HF_TOKEN`.

## Ejecutar la aplicación

Con el entorno virtual activo y el token configurado:

```powershell
python app.py
```

Luego abrir en el navegador:

```text
http://127.0.0.1:7860
```

## Notebook de análisis

El archivo:

`TP_Fava_Fernanda.ipynb`

documenta el proceso de evaluación previo a la construcción de la aplicación.

Incluye:

- definición del problema;
- selección de categorías;
- selección de dos modelos candidatos;
- conjunto de casos de prueba;
- comparación con `pipeline`;
- comparación con `InferenceClient`;
- cálculo de accuracy;
- medición de tiempos;
- análisis de resultados;
- selección del modelo final.

Para abrirlo localmente puede utilizarse Visual Studio Code con el kernel del entorno `.venv` o ejecutar:

```powershell
jupyter notebook
```

> El entorno utilizado durante el análisis contiene paquetes adicionales para trabajar con el notebook. El archivo `requirements.txt` del proyecto final contiene únicamente las dependencias necesarias para ejecutar la aplicación publicada.

## Dependencias de la aplicación

El archivo `requirements.txt` contiene:

```text
gradio
huggingface_hub
```

No se incluyen `torch` ni `transformers` porque la versión final de la aplicación utiliza inferencia remota.

## Seguridad

Para evitar la exposición de credenciales:

- el token de Hugging Face no está escrito en `app.py`;
- el token no debe almacenarse en el README ni en el notebook;
- la aplicación utiliza la variable de entorno `HF_TOKEN`;
- el entorno virtual `.venv` no debe subirse al repositorio.

## Limitaciones

La clasificación es automática y puede cometer errores, especialmente cuando:

- el mensaje es ambiguo;
- contiene más de un motivo;
- dos categorías son semánticamente similares;
- el texto aporta poco contexto.

La aplicación también depende de:

- conexión a internet;
- disponibilidad del proveedor de inferencia;
- latencia de la API;
- posibles tiempos de inicialización del servicio.

Los scores devueltos por el modelo representan confianza relativa entre las categorías candidatas y **no garantizan que la clasificación sea correcta**.

## Model cards

- [MiniLM — multilingual-MiniLMv2-L6-mnli-xnli](https://huggingface.co/MoritzLaurer/multilingual-MiniLMv2-L6-mnli-xnli)
- [mDeBERTa — mDeBERTa-v3-base-mnli-xnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli)

## Enlaces del proyecto

- [Repositorio general](https://github.com/ferfava/Seminario_Actualizacion_2026)
- [Carpeta TP_Integrador](https://github.com/ferfava/Seminario_Actualizacion_2026/tree/main/TP_Integrador)

## Aplicación publicada

**Pendiente de deploy.**

Una vez publicado el proyecto, aquí se incorporará el enlace público de la aplicación.

## Autoría y apoyo

El desarrollo, las pruebas, la comparación de modelos y las decisiones del proyecto fueron realizados por **Fernanda Andrea Fava**.

Se utilizó ChatGPT como apoyo para destrabar errores técnicos, revisar resultados y organizar la documentación.
