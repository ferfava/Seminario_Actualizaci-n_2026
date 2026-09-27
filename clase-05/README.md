# Clase 5 · Publicación y documentación

## Consigna

Publicar la app de Gradio Blocks en Render, crear y publicar una versión mínima equivalente en Streamlit, documentar ambos enlaces y las diferencias entre herramientas. Mantener el repositorio como portfolio con una carpeta y un README por clase (desde la 02), un README general y todo el código necesario para reproducir cada actividad. La entrega en el aula virtual es el enlace del repositorio.

## Archivos

- `logica.py`: función `crear_saludo` compartida por ambas interfaces.
- `gradio_app.py`: interfaz Blocks para Render.
- `streamlit_app.py`: versión mínima para Streamlit Community Cloud.
- `requirements-gradio.txt`: dependencia de Render.
- `requirements.txt`: dependencia de Streamlit Cloud.
- `render.yaml` en la raíz: configuración declarativa del servicio web de Render.

La app de la clase 4 era un ejemplo de saludos, por eso se conserva el mismo comportamiento. El objetivo de esta clase es comprobar que la misma lógica puede publicarse con dos interfaces distintas.

## Ejecutar en tu computadora

Desde esta carpeta, en un entorno virtual:

```bash
python -m pip install -r requirements-gradio.txt
python gradio_app.py
```

Para Streamlit:

```bash
python -m pip install -r requirements.txt
streamlit run streamlit_app.py
```

Ingresá un nombre, elegí un estilo y compará los resultados. Gradio usa un evento `click` que llama a `crear_saludo`. Streamlit vuelve a ejecutar el script cuando se envía el formulario. Ambas aplicaciones importan la misma función desde `logica.py`.

## Publicación

| Despliegue | Enlace verificado |
| --- | --- |
| Gradio Blocks en Render | https://seminario-actualizacion-gradio.onrender.com/ |
| Streamlit Community Cloud | https://seminarioactualizaci-n2026-4jnqjkm8rq9pkcf6onb4yl.streamlit.app/ |

### Render

La aplicación de Gradio se publicó como Web Service a partir del `render.yaml` de la raíz del repositorio. El servicio utiliza `clase-05` como directorio raíz, instala `requirements-gradio.txt` y ejecuta `python gradio_app.py`.

### Streamlit Community Cloud

La versión equivalente se publicó desde el mismo repositorio, rama `main`, utilizando como archivo principal `clase-05/streamlit_app.py`.

## Diferencias observadas

| Aspecto | Gradio Blocks | Streamlit |
| --- | --- | --- |
| Interacción | Los componentes se conectan explícitamente mediante eventos como `click` | El script se vuelve a ejecutar cuando el usuario interactúa o envía el formulario |
| Despliegue | Requiere un proceso web que escuche el puerto asignado por Render | Streamlit Community Cloud ejecuta directamente el archivo principal |
| Configuración | Se utilizó un Blueprint mediante `render.yaml` | Se configuró el repositorio, rama y ruta del archivo principal desde la plataforma |
| Lógica | Importa `crear_saludo` desde `logica.py` | Importa la misma función desde `logica.py` |
| Resultado | Aplicación pública y funcional | Aplicación pública y funcional |

La prueba permitió comprobar que la lógica de negocio puede mantenerse separada de la interfaz: ambas aplicaciones utilizan la misma función y solo cambia la forma de construir y publicar la UI.

## Checklist de entrega

- [x] Código de las dos interfaces y lógica común en GitHub.
- [x] README de esta clase y portada general con clase 5.
- [x] Gradio funcionando en Render y enlace público verificado.
- [x] Streamlit funcionando en la nube y enlace público verificado.
- [x] Enlaces incorporados al README.
- [ ] Pegar el enlace del repositorio en la tarea del aula virtual.

Documentación: [Render Web Services](https://render.com/docs/web-services) · [Streamlit Community Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy)
