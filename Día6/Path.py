from pathlib import Path

base = Path.home()
guia = Path(base,"Europa","España",Path("Barcelona","Sagrada_Familia.txt"))

guia2 = Path("Europa","España","Barcelona","Sagrada_Familia.txt")
en_europa = guia2.relative_to(Path("Europa"))
em_espania = guia2.relative_to(Path("Europa","España"))

print(en_europa)
print(em_espania)

print(guia.parent.parent.parent)