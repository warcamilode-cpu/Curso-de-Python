from rich.table import Table
from rich.console import Console

etapas     = ["Física", "Psico", "Antecedentes", "Visita", "Entrevista"]
inscritos  = [9500, 8200, 7100, 6400, 5800]
aprobados  = [8200, 6900, 6800, 5100, 5400]
dias       = [25, 20, 18, 22, 15]
equipos    = [15, 12, 10, 8, 6]
meta_dia   = [220, 180, 250, 200, 300]

tasa_aprobacion = [aprobado / inscrito * 100 for aprobado, inscrito in zip(aprobados, inscritos)]
capacidad_total = [equipo * meta * dia for equipo, meta, dia in zip(equipos, meta_dia, dias)]
menor_aprobacion = etapas[tasa_aprobacion.index(min(tasa_aprobacion))]
mayor_deficit = etapas[capacidad_total.index(min(capacidad_total))]


print(f"01. Tasa de Aprobación por Etapa: {tasa_aprobacion}")
print(f"02. Capacidad total por etapa: {capacidad_total}")
print(f"04. Etapa con menor tasa de aprobación: {menor_aprobacion}")
print(f"05. Etapa con mayor déficit de capacidad: {mayor_deficit}\n")

t = Table(title="Reporte de Etapas")
t.add_column("Nº")
t.add_column("Etapa")
t.add_column("tasa")
t.add_column("capacidad")
t.add_column("inscritos")

for i, (etapa, tasa, capacidad, inscrito) in enumerate(zip(etapas, tasa_aprobacion, capacidad_total, inscritos), start=1):
    t.add_row(
        f"{i}",
        f"{etapa}",
        f"{tasa:.2f}%",
        f"{capacidad:,}",
        f"{inscrito}",
)
Console().print(t)