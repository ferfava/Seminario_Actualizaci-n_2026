# Clase 3 · Git y organización del repositorio

La actividad de la semana pide explicar tres situaciones de la clase. Estas respuestas describen lo que se puede comprobar en este repositorio; la entrega formal de la actividad se hace en el aula virtual.

## 1. README duplicado

Hay un `README.md` en la raíz y otro en `clase-02/proyecto_integrador/`. No son dos copias en la misma ubicación: el primero presenta toda la materia y el segundo explica cómo ejecutar el proyecto de la clase 2. Los mantuve en carpetas distintas y les di propósitos diferentes para que cada nivel tenga su propia guía.

## 2. Carpeta sin ignorar

El entorno virtual `.venv` contiene paquetes instalados y archivos específicos de cada computadora, por eso no debe quedar en Git. Agregué `.venv/` al `.gitignore` antes de publicar el proyecto y comprobé que esa carpeta no aparece en el repositorio. Si ya estuviera versionada, habría que dejar de seguirla con `git rm -r --cached .venv` y luego hacer un commit, sin borrar la copia local.

## 3. Ramas `master` y `main`

El repositorio de GitHub usa la rama `main`. Para evitar confusiones, el trabajo que se sube debe apuntar a esa misma rama; se puede comprobar con `git branch --show-current` y `git remote -v`. Si un repositorio local recién creado usa `master`, se puede renombrar con `git branch -M main` antes de `git push -u origin main`. En este repositorio no hizo falta renombrar una rama: los commits visibles están en `main`.

## Ticket de salida

**¿Qué hace `git remote add origin <url>`?**  
Registra en el repositorio local la dirección del repositorio remoto y le asigna el nombre `origin`. Esto permite después usar comandos como `git push` o `git pull` indicando ese remoto. El comando por sí solo no sube archivos.

**¿Con qué me voy más tranquila hoy?**  
Me voy más tranquila entendiendo mejor la relación entre el repositorio local y GitHub, cómo comprobar en qué rama estoy trabajando y qué significa tener configurado un remoto.

**¿Con qué me voy con dudas?**  
Todavía me genera dudas qué hacer cuando el repositorio local y el remoto no están sincronizados o cuando aparece un conflicto al hacer `pull` o `push`. Es algo que necesito seguir practicando.
