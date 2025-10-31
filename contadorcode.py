from pathlib import Path

carpeta = Path(".")
lineas = 0

for archivo in carpeta.glob("organizador.py"):
    with open(archivo) as f:
        lineas += sum(1 for _ in f)

print(f"📈 Total de líneas de código: {lineas}")
