# Clase 07 — pipeline vs. InferenceClient

Fernanda Andrea Fava · Seminario de Actualización · IFTS N.º 18

## Modelo y tarea

Las cuatro aplicaciones usan `distilbert/distilbert-base-uncased-finetuned-sst-2-english` para clasificar sentimiento: POSITIVE o NEGATIVE. Lo elegí para comparar la ejecución local y remota manteniendo el mismo modelo y frases de prueba. Es un modelo preparado para inglés: la aplicación no tiene una categoría neutral ni garantiza resultados correctos en español.

Material de referencia y esqueletos: [repositorio de Cynthia M. Villagra](https://github.com/cynthiavillagra/hugging_face_models).
[Model card](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english).

## Las cuatro aplicaciones

| Archivo | Interfaz | Dónde corre el modelo |
|---|---|---|
| app_gradio_pipeline.py | Gradio | En la computadora que ejecuta Python |
| app_streamlit_pipeline.py | Streamlit | En la computadora que ejecuta Python |
| app_gradio_api.py | Gradio | En el proveedor remoto hf-inference |
| app_streamlit_api.py | Streamlit | En el proveedor remoto hf-inference |

En las aplicaciones locales se descargan los pesos y se realiza la inferencia en la PC. En las aplicaciones con API, la PC ejecuta la interfaz y envía el texto al proveedor: allí se hace la inferencia y se devuelve la respuesta. El código está guardado en GitHub, pero GitHub no ejecuta estas aplicaciones.

## Instalación en Windows

Clonar el portfolio y entrar a la carpeta:

```powershell
git clone https://github.com/ferfava/Seminario_Actualizaci-n_2026.git
cd Seminario_Actualizaci-n_2026/Clase_07
python -m venv .venv
```

No es obligatorio activar el entorno: los siguientes comandos usan directamente su intérprete.

Para las apps locales:

```powershell
.\.venv\Scripts\python.exe -m pip install -r local/requirements.txt
```

Para las apps con API:

```powershell
.\.venv\Scripts\python.exe -m pip install -r api/requirements.txt
```

Se pueden instalar ambos conjuntos en el mismo entorno para probar las cuatro apps. Las dependencias de API no incluyen torch ni transformers.

## Ejecutar las apps locales

Gradio:

```powershell
.\.venv\Scripts\python.exe app_gradio_pipeline.py
```

Streamlit:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app_streamlit_pipeline.py
```

Abrir la URL de la terminal. Gradio usa normalmente http://127.0.0.1:7860 y Streamlit http://localhost:8501. La terminal queda ocupada mientras el servidor está funcionando; Ctrl+C lo detiene. La primera carga local puede tardar por la descarga de los pesos.

## Ejecutar las apps con API

Crear un token de Hugging Face de tipo Fine-grained con permiso **Make calls to Inference Providers** en https://huggingface.co/settings/tokens. No escribirlo en el código, el README ni los commits.

El token cargado en el notebook no se comparte automáticamente con la terminal. Estos comandos solicitan el token de forma oculta y lo cargan en HF_TOKEN dentro del proceso que ejecuta la app.

Gradio:

```powershell
.\.venv\Scripts\python.exe -c "import os, runpy; from getpass import getpass; from huggingface_hub import HfApi; t=getpass('Token de Hugging Face: ').strip(); HfApi().whoami(token=t); print('Token reconocido'); os.environ['HF_TOKEN']=t; runpy.run_path('app_gradio_api.py', run_name='__main__')"
```

Streamlit:

```powershell
.\.venv\Scripts\python.exe -c "import os, sys, runpy; from getpass import getpass; os.environ['HF_TOKEN']=getpass('Token de Hugging Face: ').strip(); sys.argv=['streamlit','run','app_streamlit_api.py']; runpy.run_module('streamlit', run_name='__main__')"
```

Si Gradio muestra 0.0.0.0:7860, abrir http://127.0.0.1:7860 en el navegador. En Streamlit, presionar Enter después de escribir la frase. El reconocimiento del token valida la credencial; las consultas al modelo verifican además el acceso a inferencia.

## Qué cambió entre App 1 y App 3

Se conserva el modelo, la interfaz Gradio y la función clasificar(texto), que devuelve una etiqueta y un porcentaje.

Cambia el motor: App 1 crea un pipeline local y usa `pipe(texto)[0]`. App 3 crea un InferenceClient, necesita HF_TOKEN e internet, y llama a `client.text_classification(texto, model=MODELO)`.

Con pipeline la respuesta se lee por claves: `resultado['label']` y `resultado['score']`. Con InferenceClient se leen atributos del primer objeto: `resultado[0].label` y `resultado[0].score`.

En Streamlit se usa `@st.cache_resource` para reutilizar el pipeline o el cliente cuando el script vuelve a ejecutarse por una interacción.

## Pruebas realizadas

Resultados observados durante la ejecución; porcentajes redondeados por las interfaces.

| Frase | Resultado observado | Observación |
|---|---|---|
| I love this | POSITIVE, 100,0 % en API | Caso positivo |
| This is terrible | NEGATIVE, 100,0 % en Gradio API | Caso negativo |
| Great, another broken product. | NEGATIVE, 97,8 % en Gradio local | Coincide con el reclamo irónico |
| I expected it to be terrible, but it wasn't. | NEGATIVE, 99,1 % en las cuatro apps | Interpretación cuestionable: niega una expectativa negativa |
| The food was terribly delicious. | POSITIVE, 100 % mostrado en Gradio local | Resultado esperado en inglés |
| La comida estuvo terriblemente rica | NEGATIVE, 94,1 % en Gradio local | Error en español |
| This is a broken heart | POSITIVE, 98,3 % en Streamlit local | Interpretación cuestionable de una frase breve |
| My heart is broken and I feel devastated. | NEGATIVE, 98,9 % en Streamlit local | La reformulación con más contexto cambió el resultado |
| The food was excellent, but the service was awful | NEGATIVE, 99,4 % en Streamlit local | Una etiqueta global oculta opiniones sobre aspectos distintos |

Al separar la última frase, la comida dio POSITIVE y el servicio NEGATIVE. No se registraron sus porcentajes.

Un puntaje alto no garantiza que la interpretación sea correcta. El 100 % mostrado está redondeado. Usar una API no aumenta por sí mismo la precisión del mismo modelo.

## Problemas encontrados

- **File does not exist: app_streamlit_pipeline.py**: editar la celda no había creado el archivo. Se resolvió ejecutando la celda `%%writefile` antes de iniciar Streamlit.
- **401 Unauthorized**: se revisó el token y se recreó el cliente después de actualizar HF_TOKEN.
- **400 Bad Request en whoami**: una comprobación local mostró que la variable tenía longitud 1 y no empezaba con hf_. Se volvió a ingresar el token con getpass; la validación devolvió "Token reconocido" y la app pudo consultar el modelo.

## Límites

Las etiquetas son binarias, el modelo está preparado para inglés y puede fallar con ambigüedad, negaciones o ironía. Las apps remotas envían el texto al proveedor y dependen de internet, permisos, disponibilidad y cuotas del servicio. Las apps locales dependen de memoria, disco y capacidad del equipo.

Las apps se probaron localmente; este trabajo no incluye un deploy público. Publicar la app de API en Render es un extra opcional de la actividad.

## Ayuda utilizada

Usé ChatGPT para completar los TODO de los esqueletos de clase, entender los resultados, resolver errores de ejecución y autenticación, y organizar la documentación. Ejecuté las cuatro aplicaciones y las frases de prueba durante la actividad.
