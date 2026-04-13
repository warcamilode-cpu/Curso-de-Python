convocatoria = "INPEC 2024"
cargos     = ["Dragoneante", "Profesional", "Técnico", "Auxiliar"]
vacantes   = [800, 150, 200, 300]
inscritos  = [12000, 2800, 4100, 5500]
aprobados  = [1200, 180, 310, 420]
salarios   = [2800000, 5200000, 3500000, 2200000]

relacion_inscrito_vacante = [inscrito / vacante for inscrito, vacante in zip(inscritos, vacantes)]
tasa_aprobacion = [aprobado / inscrito * 100 for aprobado, inscrito in zip(aprobados, inscritos)]
cargo_mas_competido = cargos[relacion_inscrito_vacante.index(max(relacion_inscrito_vacante))]
tasa_menos_aprobado = [aprobado - inscrito for aprobado, inscrito in zip(aprobados, inscritos)]
cargo_menos_competido = cargos[tasa_menos_aprobado.index(min(tasa_menos_aprobado))]




for cargo, relacion in zip(cargos, relacion_inscrito_vacante):
    print(f"Relación inscritos/vacantes para {cargo}: {relacion:.2f}%")

for cargo, tasa in zip(cargos, tasa_aprobacion):
    print(f"Tasa de aprobación para {cargo}: {tasa:.2f}%")

print(f"\nEl cargo más competido es: {cargo_mas_competido}")
print(f"Cargo con menor tasa de aprobación: {cargo_menos_competido}")
print(f"05. A) Total de vacantes: {sum(vacantes)}")
print(f"05. B) Total de inscritos: {sum(inscritos)}")
print(f"05. C) Total de aprobados : {sum(aprobados)}")