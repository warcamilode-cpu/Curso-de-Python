# 01. Empleado con mayor y menor salario
# 02. Lista de empleados con salario mayor a 3000 — con comprehension
# 03. Lista de salarios ordenada de mayor a menor — sin modificar la original
# 04. Reporte numerado: nombre, salario y si está por encima o por debajo del promedio — operador ternario
from rich.table import Table
from rich.console import Console


empleados  = ["Rosa", "Diego", "Lucia", "Mario", "Sara"]
salarios   = [2800, 4200, 3100, 5500, 1900]
antiguedad = [3, 8, 2, 12, 1]   # años

salario_mayor = [empleado for empleado, salario in zip(empleados, salarios) if salario > 3000]
N_salarios = sorted(salarios, reverse=True)
promedio = sum(salarios) / len(empleados)
 


print(f"Empleado con menor salario: {empleados[salarios.index(min(salarios))]}")
print(f"Empleado con mayor salario: {empleados[salarios.index(max(salarios))]}")

print(f"\nEmpleados con salario > 3000: {list(salario_mayor)}")
print(f"El Promedio de salarios en la empresa es de: {promedio:,.0f}")

tabla_reporte = Table(title="\nReporte de Empleados")
tabla_reporte.add_column("N°")
tabla_reporte.add_column("Empleado")
tabla_reporte.add_column("Salario")
tabla_reporte.add_column("¿Por encima del Promedio?", justify="center")

for i, (empleado, salario) in enumerate(zip(empleados, salarios), start=1):

    tabla_reporte.add_row(
        f"{i:0d}",
        f"{empleado}",
        f"{salario:,}",
        f"{'SI' if salario >= promedio else 'NO'}"
    )

Console().print(tabla_reporte)
    