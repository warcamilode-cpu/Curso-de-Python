from rich.table import Table
from rich.console import Console

procesos  = ["Admisión", "Valoración", "Visita", "Entrevista"]
meta      = [500, 450, 400, 350]
real      = [480, 510, 360, 390]

dif = [rea - met for rea, met in zip(real, meta) if rea > met]
superaron = [proceso for proceso, rea, met in zip(procesos, real, meta) if rea > met]
no_superaron = [proceso for proceso, rea, met in zip(procesos, real, meta) if rea < met]
superaron2 = ["supero" if real > meta else "No supero"]

print(f"Diferencia: {dif}\n")
print(f"Procesos que superaron la meta: {superaron}")
print(f"Procesos que NO superaron la meta: {no_superaron}\n")
print(f"Mayor superávit:{procesos[meta.index(max(meta))]} - Mayor déficit:{procesos[meta.index(min(meta))]}\n")

t =Table(title="Reporte")
t.add_column("Proceso")
t.add_column("¿Supero?", justify="center")

for proceso, rea, met in zip(procesos, real, meta):
    t.add_row(
        f"{proceso}",
        f"{'SI' if rea >= met else 'No'}"
    )

Console().print(t)