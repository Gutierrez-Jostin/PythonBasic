#Tuplas
mi_tupla = (2, 4)
print("Mi tupla: ", mi_tupla)

#Lista
mi_lista = [1, 3.1416, "Jostin", mi_tupla]
print("El primer elemento de mi lista: ", mi_lista[0])
print("El primer elemento de mi lista: ", mi_lista[3])
print("El primer elemento de mi lista: ", mi_lista[2])

#Diccionarios
mi_diccionario = {
    "mi_lista": mi_lista,
    "nombre": "Jostin",
    "pi": 3.1416,
    "Tel": "663-1182238"
}
print("Llave para acceder a mi diccionario mi_lista", mi_diccionario["mi_lista"])
print("Llave para acceder a mi diccionario pi", mi_diccionario["pi"])
print("Llave para acceder a mi diccionario tel", mi_diccionario["Tel"])
