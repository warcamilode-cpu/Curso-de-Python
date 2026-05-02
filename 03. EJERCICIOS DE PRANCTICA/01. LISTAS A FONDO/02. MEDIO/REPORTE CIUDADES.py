#01.Carpetas por analista por sede — comprehension con zip
#02.Sede más productiva (mayor carpetas/analista)
#03.Sede menos productiva
#04.Reporte numerado con enumerate + zip
from rich.table import Table
from rich.console import Console

sedes      = ["Bogotá", "Medellín", "Cali", "Pasto", "Pereira"]
carpetas   = [3200, 1800, 2100, 900, 1400]
analistas  = [15, 8, 10, 4, 6]

carpetaa = [carpeta / analista for carpeta, analista in zip(carpetas, analistas)]

print(f"Carpetas por analista: {carpetaa}")
print(f"Sede más productiva: {sedes[carpetaa.index(max(carpetaa))]}")
print(f"Sede menos productiva: {sedes[carpetaa.index(min(carpetaa))]}\n")

t=Table(title="\nreporte")
t.add_column("N°", justify="center")
t.add_column("sede")
t.add_column("carpeta")
t.add_column("Cant. analista", justify="center")

for i, (sede, carpeta, analista) in enumerate(zip(sedes, carpetas, analistas), start=1):
    t.add_row(
              f"{i}",
              f"{sede}",
              f"{carpeta:,}",
              f"{analista}"
    )
    
Console().print(t)