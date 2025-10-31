import os, shutil
from pathlib import Path

# Carpeta de Descargas
base = Path.home() / "Downloads"
# Tipos de carpetas por extensión
cats = {".pdf":"PDFs", ".jpg":"Imágenes", ".png":"Imágenes", ".zip":"Comprimidos"}

for file in base.iterdir():
    if file.is_file():
        folder = cats.get(file.suffix.lower(), "Otros")
        dest = base / folder
        dest.mkdir(exist_ok=True)
        shutil.move(str(file), str(dest / file.name))

print("Organización completa ✅")
