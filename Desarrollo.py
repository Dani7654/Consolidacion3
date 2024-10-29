# Listas de nombres
nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]
magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]
otros = [nombre for nombre in nombres if nombre not in magos and nombre not in cientificos]

def hacer_grandioso():
    """Modifica la lista de magos añadiendo 'El gran' antes de cada nombre."""
    for i in range(len(magos)):
        magos[i] = f"El gran {magos[i]}"

def imprimir_nombres(lista):
    """Imprime el nombre de cada persona de la lista dada."""
    for nombre in lista:
        print(nombre)

# Imprimir la lista completa antes de ser modificada
print("Lista completa de nombres antes de ser modificados:")
imprimir_nombres(nombres)
print()

# Modificar la lista de magos
hacer_grandioso()

# Imprimir los nombres de los magos grandiosos
print("Nombres de los magos grandiosos:")
imprimir_nombres(magos)
print()

# Imprimir los nombres de los científicos
print("Nombres de los científicos:")
imprimir_nombres(cientificos)
print()

# Imprimir los nombres de los otros
print("Nombres de los otros:")
imprimir_nombres(otros)