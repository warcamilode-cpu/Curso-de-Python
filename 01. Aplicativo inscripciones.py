niveles = ["Bachiller", "Técnico Profesional", "Tecnológo", "Especialización Técnica", "Especialización Tecnologica", "Profesional", "Especialización", "Maestría", "Doctorado", "Postdoctorado"]
folios = ["Sí", "No"]
Experiencia = ["Relacionada", "Laboral", "Profesional Relacionada", "Profesional", "Docente", "No Aplica"]

def mostrar_opciones(lista, titulo):

    print(f"\n{titulo}:")
    for i, opcion in enumerate(lista, 1):
        print(f"{i}. {opcion}")
    
    while True:
        try:
            seleccion = int(input(f"Seleccione una opción (1-{len(lista)}): "))
            if 1 <= seleccion <= len(lista):
                return lista[seleccion - 1]
            else:
                print(f"Por favor, ingrese un número entre 1 y {len(lista)}")
        except ValueError:
            print("Por favor, ingrese un número válido")

print("\n=== Ingrese los Datos Básicos ===\n")
Nombre = str(input("Nombre y Apellidos: "))
cc = str(input("N° de identificación: "))
correo = str(input("Correo Electrónico: "))

print("\n=== Ingrese los Datos de Formación ===\n")

print("=== Ingrese los Datos del Pregrado ===\n")
Pregrado = [
    mostrar_opciones(niveles, "Nivel de educación"),
    str(input("Nombre de la Institución: ")), 
    str(input("Nombre del programa: ")), 
    str(input("Fecha de grado: ")), 
    mostrar_opciones(folios, "Folio válido"),
    str(input("Observación: ")) 
]

def obtener_posgrado():
    """Pregunta al usuario si desea ingresar datos de posgrado"""
    respuesta_posgrado = input("\n¿Solicita posgrado? (SÍ/NO): ").upper()
    
    if respuesta_posgrado in ['S', 'SI', 'SÍ', 'YES']:
        print("\n=== Ingrese los Datos del Posgrado ===\n")
        
        Posgrado = [
            mostrar_opciones(niveles, "Nivel de educación"),
            str(input("Nombre de la Institución: ")), 
            str(input("Nombre del programa: ")), 
            str(input("Fecha de grado: ")), 
            mostrar_opciones(folios, "Folio válido"),
            str(input("Observación: ")) 
        ]
        return Posgrado
    else:
        return None

Posgrado = obtener_posgrado()

def obtener_informal():
    """Pregunta al usuario si desea ingresar datos de educación informal"""
    respuesta_informal = input("\n¿Solicita Educación informal? (SÍ/NO): ").upper()
    
    if respuesta_informal in ['S', 'SI', 'SÍ', 'YES']:
        print("\n=== Ingrese los Datos de la Educación Informal ===\n")
        
        informal = [
            str(input("Intensidad Horaria: ")),
            str(input("Nombre de la Institución: ")), 
            str(input("Nombre del programa: ")), 
            str(input("Fecha de grado: ")), 
            mostrar_opciones(folios, "Folio válido"),
            str(input("Observación: ")) 
        ]
        return informal
    else:
        return None

informal = obtener_informal()

print("\n=== EXPERIENCIA ===\n")

Certificados_exp = int(input("Número de certificados expedidos: "))
i = 1
todos_los_certificados = []

for i in range(Certificados_exp):
    print(f"\n=== Ingrese los Datos del Certificado {i+1} ===\n")
    Certificados = [
        str(input("Empresa o Entidad: ")), 
        str(input("Cargo: ")), 
        str(input("Fecha ingreso: ")), 
        str(input("Fecha salida: ")),
        mostrar_opciones(folios, "Folio válido"),
        mostrar_opciones(Experiencia, "Tipo de Experiencia"),
        str(input("Observación: ")) 
    ]
    i += 1

    todos_los_certificados.append(Certificados)

# Mostrar resultados
print("\n=== Resumen de Datos ===")

print("\n=== DATOS BÁSICOS ===\n")
print(f"Nombre: {Nombre}")
print(f"Identificación: {cc}")
print(f"Correo: {correo}")

print("\n=== FORMACIÓN ===\n")
print(f"Pregrado: {Pregrado}")

if Posgrado:
    print(f"Posgrado: {Posgrado}")
else:
    print("Posgrado: No solicitado")

if informal:
    print(f"Educación Informal: {informal}")
else:
    print("Educación Informal: No solicitado")

print("\n=== EXPERIENCIA ===\n")

if todos_los_certificados:
    for i, certificado in enumerate(todos_los_certificados):
        print(f"Certificado {i+1}, Empresa o Entidad: {certificado[0]}, Cargo: {certificado[1]}, Fecha ingreso: {certificado[2]}, Fecha salida: {certificado[3]}, Folio válido: {certificado[4]}, Tipo de experiencia: {certificado[5]}, Observación: {certificado[6]}:"),
else:
    print("No se ingresaron certificados.")