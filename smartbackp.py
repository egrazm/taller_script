import shutil, datetime
from pathlib import Path

src= Path.home() /"Documents"
backup= Path.home()/"Backups"
backup.mkdir(exist_ok=True)

fecha = datetime.date.today().strftime("%Y%m%d")
zip_name= backup /f"respaldo_{fecha}"

shutil.make_archive(zip_name, "zip", src)

print(f"Backup creado: {zip_name}.zip ✅")