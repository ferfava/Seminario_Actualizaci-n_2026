# Clase 2 · Preparación del entorno

Esta actividad configura un proyecto Python con VS Code, un entorno virtual, una dependencia y control de versiones con Git. El código de `app.py` comprueba que la dependencia se importa desde el entorno activo.

## Archivos

- `app.py`: programa mínimo de verificación.
- `requirements.txt`: dependencia que utiliza el programa.
- `.gitignore`: excluye el entorno virtual y archivos generados.

## Reproducir en Windows (PowerShell)

Desde esta carpeta:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

En VS Code, abrir esta carpeta y elegir **Python: Select Interpreter** → `.venv\Scripts\python.exe`. Si PowerShell bloquea la activación, se puede ejecutar directamente `.\.venv\Scripts\python.exe app.py` y usar ese intérprete en VS Code.

Para verificar el intérprete y el historial del repositorio, desde la carpeta abierta en VS Code:

```powershell
python -c "import sys; print(sys.executable)"
git log --oneline
```

Las salidas de esos comandos dependen de cada computadora y del historial real: no se incluyen resultados simulados. El entorno `.venv` se crea localmente y está excluido de Git.

## Consigna

1. Verificar Python, VS Code y Git, y configurar el nombre de Git.
2. Crear el proyecto con `app.py` y `README.md`.
3. Crear y seleccionar `.venv` en VS Code.
4. Instalar una biblioteca y registrar las dependencias.
5. Revisar el estado de Git y registrar el primer commit.

El ticket de salida de la clase solicita pegar las salidas reales de los dos comandos anteriores y responder una pregunta conceptual. Es una actividad distinta del laboratorio.
