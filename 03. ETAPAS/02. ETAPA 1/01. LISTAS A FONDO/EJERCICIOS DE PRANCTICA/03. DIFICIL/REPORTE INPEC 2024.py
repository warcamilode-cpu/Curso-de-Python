#01. Relación inscritos/vacante por cargo — comprehension
#02. Tasa de aprobación por cargo
#03. Cargo más competido (mayor relación inscritos/vacante)
#04. Cargo con menor tasa de aprobación
#05. Total de vacantes, inscritos y aprobados — sum()
#06. Lista de cargos ordenada por salario de mayor a menor — sorted con zip
#07. Reporte ejecutivo completo con rich Table

from rich.table import Table
from rich.console import Console

convocatoria = "INPEC 2024"
cargos     = ["Dragoneante", "Profesional", "Técnico", "Auxiliar"]
vacantes   = [800, 150, 200, 300]
inscritos  = [12000, 2800, 4100, 5500]
aprobados  = [1200, 180, 310, 420]
salarios   = [2800000, 5200000, 3500000, 2200000]

relacion_inscrito_vacante = [inscrito / vacante for inscrito, vacante in zip(inscritos, vacantes)]
tasa_aprobacion = [aprobado / inscrito * 100 for aprobado, inscrito in zip(aprobados, inscritos)]
cargo_mas_competido = cargos[relacion_inscrito_vacante.index(max(relacion_inscrito_vacante))]
cargo_menor_tasa = cargos[tasa_aprobacion.index(min(tasa_aprobacion))]

nueva = sorted(salarios, reverse=True)
for cargo, relacion in zip(cargos, relacion_inscrito_vacante):
    print(f"Relación inscritos/vacantes para {cargo}: {relacion:.2f}%")

for cargo, tasa in zip(cargos, tasa_aprobacion):
    print(f"Tasa de aprobación para {cargo}: {tasa:.2f}%")

print(f"\n03. El cargo más competido es: {cargo_mas_competido}")
print(f"04. Cargo con menor tasa de aprobación: {cargo_menor_tasa}")
print(f"05. A) Total de vacantes: {sum(vacantes)}")
print(f"05. B) Total de inscritos: {sum(inscritos)}")

print(f"06. cargos por salario:")
pares = sorted(zip(salarios, cargos), reverse=True)
for salario, cargo in pares:
    print(f"{cargo} — {salario:,.0f} $")


t = Table(title="07. Reporte Ejecutivo")
t.add_column("N°")
t.add_column("Cargos")
t.add_column("Vacantes")
t.add_column("Inscritos")
t.add_column("Aprobados")
t.add_column("Salarios")
t.add_column("Relacion Incritos")
t.add_column("Tasa de Aprobacion")

for i, (cargo, vancante, inscrito, aprobado, salario, relacion, tasa) in enumerate(zip(cargos, vacantes, inscritos, aprobados, salarios, relacion_inscrito_vacante, tasa_aprobacion), start=1):
    t.add_row(
        f"{i:02d}",
        f"{cargo}",
        f"{vancante}",
        f"{inscrito:,}",
        f"{aprobado:,}",
        f"{salario:,.2f} $",
        f"{relacion:.2f}",
        f"{tasa:.2f}"
    )

Console().print(t)