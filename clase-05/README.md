# Clase 5 · Publicación y documentación

## Consigna

Publicar la app de Gradio Blocks en Render, crear y publicar una versión mínima equivalente en Streamlit, documentar ambos enlaces y las diferencias entre herramientas. Mantener el repositorio como portfolio con una carpeta y un README por clase (desde la 02), un README general y todo el código necesario para reproducir cada actividad. La entrega en el aula virtual es el enlace del repositorio.

## Archivos

- logica.py: función crear_saludo compartida por ambas interfaces.
- gradio_app.py: interfaz Blocks para Render.
- streamlit_app.py: versión mínima para Streamlit Community Cloud.
- requirements-gradio.txt: dependencia de Render.
- requirements.txt: dependencia de Streamlit Cloud.
- render.yaml en la raíz: configuración declarativa del servicio web de Render.

La app de la clase 4 era un ejemplo de saludos, por eso se conserva el mismo comportamiento. El valor de esta clase es comprobar que la lógica funciona con dos interfaces distintas. Si la aplicación real de cursada es otra, hay que adaptar ambas interfaces a su procedimiento antes de entregar.

## Ejecutar en tu computadora

Desde esta carpeta, en un entorno virtual:

    python -m pip install -r requirements-gradio.txt
    python gradio_app.py

En otro entorno virtual (o después de instalar requirements.txt):

    python -m pip install -r requirements.txt
    streamlit run streamlit_app.py

Ingresá un nombre, elegí un estilo y compará los resultados. Gradio usa un evento click que llama a crear_saludo. Streamlit vuelve a ejecutar el script cuando se envía el formulario. Ambas aplicaciones importan la misma función de logica.py.

## Publicación

**Render:** vinculá este repositorio y usá el archivo render.yaml como Blueprint, o creá un Web Service Python con directorio raíz clase-05, build command ` pip install -r requirements-gradio.txt ` y start command ` python gradio_app.py `. Render define PORT; gradio_app.py escucha en 0.0.0.0 y ese puerto. Verificá el resultado desde el enlace público, no solo los logs.

**Streamlit Community Cloud:** creá una app desde este repositorio, rama main, archivo principal clase-05/streamlit_app.py. La dependencia está en clase-05/requirements.txt. Verificá el formulario en el enlace público.

| Despliegue | Enlace verificado |
| --- | --- |
| Gradio Blocks en Render | Pendiente de publicar y verificar |
| Streamlit | Pendiente de publicar y verificar |

## Diferencias observadas en la implementación

| Aspecto | Gradio Blocks | Streamlit |
| --- | --- | --- |
| Interacción | Un botón conecta entradas y salida mediante click | Un formulario envía valores y vuelve a ejecutar el script |
| Despliegue | Proceso web que escucha el puerto de Render | Streamlit Community Cloud ejecuta el archivo principal |
| Lógica | Importa crear_saludo de logica.py | Importa la misma función |

Estas son diferencias del código, no una evaluación de rendimiento ni de la experiencia de despliegue. Completá la comparación con lo que efectivamente ocurra al publicar.

## Checklist de entrega

- [x] Código de las dos interfaces y lógica común en GitHub.
- [x] README de esta clase y portada general con clase 5.
- [ ] Gradio funcionando en Render y enlace público verificado.
- [ ] Streamlit funcionando en la nube y enlace público verificado.
- [ ] Sustituir los pendientes de la tabla por los dos enlaces reales.
- [ ] Pegar el enlace del repositorio en la tarea del aula virtual.

Documentación: [Render Web Services](https://render.com/docs/web-services), [Streamlit Community Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy).
