# Clase 4 · Gradio Blocks

## Consigna

Modificar la interfaz de la aplicación con Gradio Blocks en lugar de `Interface`; sumar un componente diferente de `Textbox` y `Button`; conectar una función propia que reciba parámetros y devuelva un resultado. La actividad también contemplaba probar la aplicación y compartir una versión pública.

## Implementación

El archivo `app.py` contiene una aplicación construida con Gradio Blocks. Recibe un nombre mediante un `Textbox` y permite elegir un estilo con un `Dropdown`, incorporando así un componente adicional. La función `crear_saludo(nombre, estilo)` procesa ambos parámetros y devuelve el resultado en un componente de salida cuando se presiona el botón.

La estructura deja separada la lógica de la interacción visual y sirve como base para la publicación realizada posteriormente en la Clase 5.

## Ejecución local

Desde `clase-04`, crear y activar un entorno virtual, instalar las dependencias y ejecutar la aplicación:

```bash
python -m venv .venv
python -m pip install -r requirements.txt
python app.py
```

Activación del entorno virtual:

- Linux/macOS: `source .venv/bin/activate`
- Windows PowerShell: `.venv\Scripts\Activate.ps1`

Al iniciar la aplicación, Gradio muestra una URL local y, cuando se habilita el modo compartido, puede generar un enlace público temporal.

## Resultado

La actividad quedó implementada en este repositorio con:

- [x] Interfaz construida con Gradio Blocks.
- [x] Uso de `Dropdown` además de `Textbox` y `Button`.
- [x] Función propia con parámetros y valor de retorno.
- [x] Código y dependencias necesarios para reproducir la aplicación.
- [x] Continuidad del mismo ejemplo en la Clase 5, donde la aplicación fue publicada y verificada en Render y se creó una versión equivalente en Streamlit.

La publicación permanente y la comparación entre interfaces están documentadas en [`clase-05/README.md`](../clase-05/README.md).

Referencias: [Blocks](https://www.gradio.app/docs/gradio/blocks) · [Compartir una app](https://www.gradio.app/guides/sharing-your-app)
