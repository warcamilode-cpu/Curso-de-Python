#01 Tiempo máximo y mínimo
#02 Lista ordenada de menor a mayor sin modificar la original
#03 ¿Cuántos tiempos superan el promedio?
#04 Lista con solo los tiempos redondeados al entero más cercano — round()

tiempos = [3.5, 7.2, 2.1, 8.4, 5.0, 4.3, 6.8]

promedio = sum(tiempos) / len(tiempos)
aprobado = [maximo for maximo in tiempos if maximo > promedio]
redondeo = [round(tiempo) for tiempo in tiempos]

print(f"Tiempo maximo es de: {max(tiempos)}")
print(f"Tiempo minimo es de: {min(tiempos)}")

print(f"El promedio de tiempos es de: {promedio:.2f}")
print(f"Los tiempos por encima del promedio son: {aprobado}")
print(f"Los tiempos redondeados son: {redondeo}")