from rich.table import Table
from rich.console import Console

archivos = ["documento.dox", "documento.pdf", "documento.xlsx"]

t = Table(title= "extenciones")
t.add_column("Archivo")
t.add_column("Nombre")
t.add_column("Extension")

for i in archivos:
    nombre = i[:i.index('.')]
    extension = i[i.index('.')+1:]

    t.add_row(
        f"{i}",
        f"({nombre})",
        f"({extension})"
    )

Console().print(t)
#hola