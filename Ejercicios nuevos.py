#Ejercicio 1
# palabras = ["gato", "elefante", "sol", "computadora", "mesa", "bicicleta"]
# 
# cortas = [i for i in palabras if len(i) <= 5]
# largas = [i for i in palabras if len(i) > 5]
# 
# # print(cortas)
# print(largas)

#Ejercicio 2
# texto = "Hola mundo, esto es Python"
# vocales = "aeiouAEIOU"
# 
# coleccion = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
# 
# for i in texto.lower():
#     if i in vocales:
#         coleccion[i] += 1
# print(coleccion)

#Ejercicio 3
# 
# inventario = {"manzanas": 10, "peras": 3, "uvas": 0, "mangos": 7}
# 
# print("\nAgregar/actualizar Inventario\n")
# clav_mas = input("Ingrese la clave que desea agregar/actualizar: ")
# val_mas = int(input("Ingrese el valor que desea agregar/actualizar: "))
# inventario[clav_mas] = val_mas
# print("\nInventario actualizado:")
# print(inventario)
# 
# print("\nEliminar del Inventario")
# clav_menos = input("\nIngrese el producto a eliminar: ")
# if clav_menos in inventario:
#     del inventario[clav_menos]
#     print("\nInventario actualizado:")
#     print(inventario)
# else:
#     print("El producto no existe")
# 
# print("\nProductos con stock menor")
# stock = int(input("\nIngrese el valor con el que quiere medir el inventario: "))
# inventario_bajo = [k for k, v in inventario.items() if v <= stock]
# print(f"Productos con stock bajo: {inventario_bajo}")

#Ejercicio 4

# agenda = {
#     "ana":  {"telefono": "555-1234", "email": "ana@mail.com"},
#     "luis": {"telefono": "555-5678", "email": "luis@mail.com"},
#     "camilo": {"telefono": "555-4598", "email": "camilo@mail.com"},
# }
# 
# 
# for i, contacto in sorted(agenda.items()):
#     print(f"{i} - {contacto['telefono']} - {contacto['email']}") 
# 
# 
# nombre = input("\nAgregue el nombre del contacto: ").lower()
# 
# if nombre in agenda:
#     contacto = agenda[nombre]
#     print(f"Nombre: {nombre}")
#     print(f"Teléfono: {contacto['telefono']}")
#     print(f"Email: {contacto['email']}")
# else:
#     print("Contacto no encontrado")

#Ejercicio 5
# 
# estudiantes = [
#     {"nombre": "Carlos", "notas": [8, 9, 7, 10]},
#     {"nombre": "Sofia",  "notas": [6, 7, 9, 8]},
#     {"nombre": "Pedro",  "notas": [10, 10, 9, 10]},
# ]
# 
# promedios = {}
# mejor_estudiante = ""
# mejor_promedio = 0
# 
# for est in estudiantes:
#     nombre = est["nombre"]
#     notas = est["notas"]
#     
#     promedio = sum(notas) / len(notas)
#     promedios[nombre] = promedio
#     
#     if promedio > mejor_promedio:
#         mejor_promedio = promedio
#         mejor_estudiante = nombre
# 
# print("Promedios:", promedios)
# print("Mejor estudiante:", mejor_estudiante)

#Ejercicio 6
# 
# carrito = {
#     "leche":  {"precio": 1.50, "cantidad": 2},
#     "pan":    {"precio": 0.80, "cantidad": 3},
#     "huevos": {"precio": 3.90, "cantidad": 4}
# }
# 
# carrito_completo = 0
# 
# for k, v in carrito.items():
#     total_producto = v["precio"] * v["cantidad"]
#     carrito_completo += total_producto
#     print(f"{k:<10} X{v['cantidad']} → ${total_producto:.2f}")
# 
# print(f"TOTAL → ${carrito_completo:.2f}")























