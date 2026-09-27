# Clase 4 · Gradio Blocks

## Consigna

Modificar la interfaz de la aplicación con Gradio Blocks en lugar de Interface; sumar un componente diferente de Textbox y Button; conectar una función propia que reciba parámetros y devuelva un resultado. Correr la app localmente con share=True, verificar el enlace público y entregarlo en el aula virtual. El ticket de salida pide el enlace actualizado del Space de Hugging Face y una captura de la app funcionando, o del error si no arranca.

## Implementación

El archivo app.py ofrece una aplicación de ejemplo en Blocks. Recibe un nombre en un Textbox y un estilo en un Dropdown (componente nuevo). La función crear_saludo(nombre, estilo) devuelve un mensaje al Textbox de salida al hacer clic en el botón.

Es una base reproducible para la consigna. Si la app creada en clase tiene otro propósito, se pueden incorporar el Dropdown y la función a esa app sin reemplazar su lógica.

## Ejecución local

Desde clase-04, crear y activar un entorno virtual, instalar las dependencias y correr la aplicación:

    python -m venv .venv
    python -m pip install -r requirements.txt
    python app.py

Activación: Linux/macOS: source .venv/bin/activate. Windows PowerShell: .venv\Scripts\Activate.ps1.

La terminal mostrará la URL local y, cuando Gradio pueda establecer la conexión, un enlace temporal público de gradio.live. Mantené el proceso abierto mientras se evalúa la entrega. Para publicar un Space permanente, copiá app.py y requirements.txt a tu Space de Hugging Face y verificá allí que arranque. No se incluye un enlace ni una captura inventados: ambos dependen de una ejecución y un Space propios.

## Pendiente para entregar en el aula

- [ ] Ejecutar la app y probar las opciones del Dropdown.
- [ ] Pegar en el aula el enlace temporal generado al correr app.py.
- [ ] Actualizar y verificar el Space; pegar su enlace público en el ticket de salida.
- [ ] Adjuntar una captura real de la app en Blocks (o del error) y describir en una línea dónde quedó el trabajo.

Referencias: [Blocks](https://www.gradio.app/docs/gradio/blocks) y [Compartir una app](https://www.gradio.app/guides/sharing-your-app).
