from rich.table import Table
from rich.console import Console

meses      = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
ingresos   = [45000, 52000, 48000, 61000, 55000, 70000]
gastos     = [38000, 41000, 45000, 39000, 48000, 52000]
meta_ing   = 50000

utilidad = [ingreso - gasto for ingreso, gasto in zip(ingresos, gastos)]
utilidad_negativa = [mes for mes, util in zip(meses, utilidad) if util < 0]
utilidad_positiva = [mes for mes, ing in zip(meses, ingresos) if ing > meta_ing]
mas_rentable = meses[utilidad.index(max(utilidad))]
menos_rentable = meses[utilidad.index(min(utilidad))]
promedio = sum(utilidad) / len(meses)

t0 = Table(title="01. Reporte de Utilidad Mensual")
t0.add_column("Nº")
t0.add_column("Mes")
t0.add_column("utilidad")

for i, (mes, util) in enumerate(zip(meses, utilidad), start=1):
    t0.add_row(
        f"{i}",
        f"{mes}",
        f"{util:,}"
    )

t = Table(title="06. Reporte Mensual")
t.add_column("Nº")
t.add_column("Mes")
t.add_column("ingresos")
t.add_column("gastos")
t.add_column("utilidad")

for i, (mes, ingreso, gasto, util) in enumerate(zip(meses, ingresos, gastos, utilidad), start=1):
    t.add_row(
        f"{i}",
        f"{mes}",
        f"{ingreso:,}",
        f"{gasto:,}",
        f"{util:+,}"
    )
Console().print(t0)

print(f"02. Meses con utilidad negativa: {utilidad_negativa}")
print(f"03. Meses con utilidad positiva: {utilidad_positiva}")
print(f"04. A) Meses con mayor utilidad: {mas_rentable}")
print(f"04. B) Meses con menor utilidad: {menos_rentable}")
print(f"05. Promedio de utilidad mensual: {promedio:,.2f}")

Console().print(t)