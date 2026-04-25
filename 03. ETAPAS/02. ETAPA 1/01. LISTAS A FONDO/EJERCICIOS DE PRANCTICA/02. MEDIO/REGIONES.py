regiones   = ["Norte", "Sur", "Oriente", "Occidente", "Centro"]
inscritos  = [1200, 850, 1050, 920, 1400]
cupos      = [1000, 900, 800, 1100, 1200]

reg_mas_inscritos = [region for region, cupo, inscrito in zip(regiones, cupos, inscritos) if cupo < inscrito]
reg_disponible = [region for region, cupo, inscrito in zip(regiones, cupos, inscritos) if cupo >= inscrito]
dif = [ cupo - inscrito for cupo, inscrito in zip(cupos, inscritos)]
mayor_exceso = regiones[dif.index(min(dif))]
mayor_disponibilidad = regiones[dif.index(max(dif))]

print(f"Regiones con más inscritos que cupos: {reg_mas_inscritos}")
print(f"Regiones con cupos disponibles: {reg_disponible}")
print(f"Diferencia inscritos vs cupos por región: {dif}")
print(f"Región con mayor exceso de inscritos: {mayor_exceso}")
print(f"Región con mayor disponibilidad de cupos: {mayor_disponibilidad}")