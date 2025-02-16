# Lista de nombres
nombres = ["Ana", "Juan", "Pedro", "Luisa"]

# Usamos enumerate() para recorrer la lista con índices
for indice, nombre in enumerate(nombres):
    print(f"Índice: {indice}, Nombre: {nombre}")


#Usamos un bucle for con la función enumerate(nombres).
#enumerate() devuelve un par (índice, valor) en cada iteración.
#En cada iteración, indice toma el valor del índice actual y nombre toma el valor correspondiente de la lista.
#print(f"Índice: {indice}, Nombre: {nombre}") imprime cada índice junto con su nombre.
