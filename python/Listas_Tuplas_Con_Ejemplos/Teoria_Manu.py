def main():
    print("*****  TEORÍA DE PYTHON  *****")
    
    print("1. Listas")
    # Formas de crear una lista
    miLista = []
    miLista2 = [1, 7, 4, 6, 2]
    miLista3 = list("12345")
    # Métodos de las listas
    miLista.append(2)       # Añadir
    miLista2.remove(6)      # Eliminar
    print(miLista3)         # Mostrar
    print(miLista2[2])      # Acceder a un elemento
    # Formas de iterar una lista
    for i in range(len(miLista2)):
        print(miLista2[i])
        break
    
    print()
    print("2. Tuplas")
    # Formas de crear una tupla
    miTupla = ()
    miTupla2 = (1, 7, 4, 6, 2)
    miTupla3 = tuple(miLista2)
    # Métodos de las tuplas
    print(miTupla3)         # Mostrar
    print(miTupla2[2])      # Acceder a un elemento
    # Formas de iterar una tupla
    for i in miTupla2:
        print(i)
        break
    
    print()
    print("3. Conjuntos")
    # A tener en cuenta: los conjuntos no permiten duplicados ni tienen índice
    miConjunto = set()
    miConjunto2 = {1, 7, 4, 6, 2}
    miConjunto3 = set(miTupla2)
    # Métodos de los conjuntos
    miConjunto.add(2)       # Añadir
    miConjunto2.remove(4)   # Eliminar
    print(miConjunto3)      # Mostrar
    # Iterar conjuntos
    listaConjunto = list(enumerate(miConjunto2))
    print(listaConjunto[1])
    for i, valor in enumerate(miConjunto2):
        print(i, valor)
        break
    
    print()
    print("4. Diccionarios")
    # Formas de crear un diccionario
    miDiccionario = {}
    miDiccionario2 = {"clave1": 1, "clave2": 2, "clave3": 3}
    miDiccionario3 = dict(clave1=1, clave2=2, clave3=3)
    # Métodos de los diccionarios   
    miDiccionario["clave4"] = 4     # Añadir
    miDiccionario2.pop("clave2")    # Eliminar
    print(miDiccionario3)           # Mostrar
    print(miDiccionario2["clave1"]) # Acceder a un elemento
    # Iterar un diccionario
    for clave in miDiccionario2.keys():
        print(clave)
        break
    for valor in miDiccionario2.values():
        print(valor)
        break
    for clave, valor in miDiccionario2.items():
        print(clave, valor)
        break
    
    print()
    print("5. Trabajo con Ficheros CSV")
    import csv
    
    # Escribir en un archivo CSV
    with open("datos.csv", "w", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Nombre", "Edad", "Ciudad"])
        escritor.writerow(["Juan", 25, "Madrid"])
        escritor.writerow(["Ana", 30, "Barcelona"])
    
    # Leer un archivo CSV
    with open("datos.csv", "r") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            print(fila)
    
    # Trabajar con diccionarios en CSV
    with open("datos_dic.csv", "w", newline="") as archivo:
        campos = ["Nombre", "Edad", "Ciudad"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerow({"Nombre": "Carlos", "Edad": 22, "Ciudad": "Sevilla"})
        escritor.writerow({"Nombre": "Lucía", "Edad": 28, "Ciudad": "Valencia"})
    
    with open("datos_dic.csv", "r") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            print(fila["Nombre"], fila["Edad"], fila["Ciudad"])
    
if __name__ == "__main__":
    main()