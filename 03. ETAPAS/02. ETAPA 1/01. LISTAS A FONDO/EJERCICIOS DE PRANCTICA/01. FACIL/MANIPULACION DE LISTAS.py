#01. Agrega "Sofia" al final
#02. Inserta "Jorge" en la posición 2
#03. Elimina "Luis"
#04. Imprime la lista final ordenada alfabéticamente

analistas = ["Ana", "Luis", "Marta", "Carlos", "Pedro"]
print(analistas)

analistas.append("Sofia")
print(analistas)

analistas.insert(2, "Jorge")
print(analistas)

analistas.remove("Luis")
print(analistas)

analistas.sort()
print(analistas)