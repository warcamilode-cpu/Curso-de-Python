from rich.table import Table
from rich.console import Console

aspirantes = ["García", "López", "Martínez", "Rodríguez", "Pérez",
              "González", "Hernández", "Díaz", "Torres", "Vargas"]
puntajes   = [78, 92, 65, 88, 71, 95, 83, 69, 77, 90]
aprobatorio = 75

aprobados = [aspirante for aspirante, puntaje in zip(aspirantes, puntajes) if puntaje >= aprobatorio]
reprobados = [aspirante for aspirante, puntaje in zip(aspirantes, puntajes) if puntaje < aprobatorio]
nueva = sorted(puntajes, reverse=True)

print(f"Aspirantes aprobados: {aprobados}")
print(f"Aspirantes aprobados: {reprobados}")
print(f"Top 3 puntajes más altos: {nueva[:3]}")
print(f"García quedó en la posición: {aspirantes.index('García') + 1}")

t = Table(title="\nReporte de aspirantes")
t.add_column("Puesto")
t.add_column("Nombre")
t.add_column("Puntaje")

for i, (aspirante, puntaje) in enumerate(zip(aspirantes, puntajes), start=1):
       t.add_row(
        f"{i}",
        f"{aspirante}",
        f"{puntaje}"
    )
    
Console().print(t)