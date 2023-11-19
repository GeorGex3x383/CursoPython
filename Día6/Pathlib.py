from pathlib import Path, PureWindowsPath

carpeta = Path("C:/Users/jemil/Documents/CursosYMas/CursoPython/Día6/prueba.txt")

ruta_windows = PureWindowsPath(carpeta)

print(ruta_windows)

print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)

if not carpeta.exists():
    print("No existe")
else:
    print("Si existe")