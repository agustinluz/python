def main():
    print("*****  TEORÍA DE PYTHON  *****")
    
    # Sección 1: Listas
    print("1. Listas")
    miLista = []  # Crear una lista vacía
    miLista2 = [1, 7, 4, 6, 2]  # Crear una lista con elementos
    miLista3 = list("12345")  # Crear una lista a partir de una cadena
    miLista.append(2)  # Añadir un elemento a la lista
    miLista2.remove(6)  # Eliminar un elemento de la lista
    miLista.reverse()  # Invertir la lista
    miLista.sort()  # Ordenar la lista en orden ascendente
    miLista2.sort(reverse=True)  # Ordenar la lista en orden descendente
    print(miLista3)  # Mostrar la lista
    print(miLista2[2])  # Acceder a un elemento de la lista
    print(len(miLista2))  # Obtener el tamaño de la lista
    print(sum(miLista2))  # Obtener la suma de los elementos de la lista
    for i in miLista2:  # Iterar sobre los elementos de la lista
        print(i)
    
    # Sección 2: Tuplas
    print()
    print("2. Tuplas")
    miTupla = ()  # Crear una tupla vacía
    miTupla2 = (1, 7, 4, 6, 2)  # Crear una tupla con elementos
    miTupla3 = tuple(miLista2)  # Crear una tupla a partir de una lista
    print(miTupla3)  # Mostrar la tupla
    print(miTupla2[2])  # Acceder a un elemento de la tupla
    print(len(miTupla2))  # Obtener el tamaño de la tupla
    print(sum(miTupla2))  # Obtener la suma de los elementos de la tupla
    print(miTupla2.count(7))  # Contar las apariciones de un valor en la tupla
    
    # Sección 3: Cadenas de texto
    print()
    print("3. Cadenas de texto")
    miCadena = "Hola, mundo!"
    print(miCadena.upper())  # Convertir la cadena a mayúsculas
    print(miCadena.lower())  # Convertir la cadena a minúsculas
    print(miCadena.replace("Hola", "Adiós"))  # Reemplazar texto en la cadena
    print(miCadena.split(","))  # Dividir la cadena en una lista
    print(len(miCadena))  # Obtener la longitud de la cadena
    print(miCadena.strip())  # Eliminar espacios en blanco al inicio y final
    print(miCadena[1:5])  # Rebanado de cadena
    
    # Sección 4: Conjuntos
    print()
    print("4. Conjuntos")
    miConjunto = set()  # Crear un conjunto vacío
    miConjunto2 = {1, 7, 4, 6, 2}  # Crear un conjunto con elementos
    miConjunto3 = set(miTupla2)  # Crear un conjunto a partir de una tupla
    miConjunto.add(3)  # Añadir un elemento al conjunto
    miConjunto2.remove(4)  # Eliminar un elemento del conjunto
    print(miConjunto3)  # Mostrar el conjunto
    print(5 in miConjunto2)  # Comprobar si un elemento está en el conjunto
    print(miConjunto2.union(miConjunto3))  # Unión de conjuntos
    print(miConjunto2.intersection(miConjunto3))  # Intersección de conjuntos
    
    # Sección 5: Diccionarios
    print()
    print("5. Diccionarios")
    miDiccionario = {}  # Crear un diccionario vacío
    miDiccionario2 = {"clave1": 1, "clave2": 2, "clave3": 3}  # Crear un diccionario con elementos
    miDiccionario3 = dict(clave1=1, clave2=2, clave3=3)  # Crear un diccionario usando el constructor dict
    miDiccionario["clave4"] = 4  # Añadir un par clave-valor al diccionario
    miDiccionario2.pop("clave2")  # Eliminar un par clave-valor del diccionario
    print(miDiccionario3)  # Mostrar el diccionario
    print("clave1" in miDiccionario2)  # Comprobar si una clave existe en el diccionario
    print(miDiccionario2.get("clave1"))  # Obtener el valor de una clave sin error
    for clave, valor in miDiccionario2.items():  # Iterar sobre los pares clave-valor del diccionario
        print(clave, valor)
    print(miDiccionario2.keys())  # Obtener las claves del diccionario
    print(miDiccionario2.values())  # Obtener los valores del diccionario
    print(miDiccionario2.items())  # Obtener los pares clave-valor del diccionario
    miDiccionario2.update({"clave5": 5, "clave6": 6})  # Actualizar el diccionario con nuevos pares clave-valor
    print(miDiccionario2)
    
    # Sección 6: Trabajo con Ficheros CSV
    print()
    print("6. Trabajo con Ficheros CSV")
    import csv
    # Escritura en CSV
    with open("datos.csv", "w", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Nombre", "Edad", "Ciudad"])
        escritor.writerow(["Juan", 25, "Madrid"])
        escritor.writerow(["Ana", 30, "Barcelona"])
    # Lectura en CSV
    with open("datos.csv", "r") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            print(fila)
    # Lectura de CSV como diccionario
    with open("datos.csv", "r") as archivo:
        lector_dict = csv.DictReader(archivo)
        for fila in lector_dict:
            print(fila)
    # Escritura de CSV con diccionario
    with open("datos_dict.csv", "w", newline="") as archivo:
        campos = ["Nombre", "Edad", "Ciudad"]
        escritor_dict = csv.DictWriter(archivo, fieldnames=campos)
        escritor_dict.writeheader()
        escritor_dict.writerow({"Nombre": "Luis", "Edad": 40, "Ciudad": "Sevilla"})
    
    # Lectura de CSV desde una cadena y guardar en una lista
    print()
    print("Lectura de CSV desde una cadena y guardar en una lista")
    with open("datos.csv", "r") as archivo:
        lista_datos = []
        lector = csv.reader(datos_csv.splitlines())
        for fila in lector:
            lista_datos.append(fila)
    
        for fila in lista_datos:
            print(fila)
    
    # Ordenar un fichero CSV por uno de los elementos internos (por ejemplo, Edad)
    print()
    print("Ordenar CSV por Edad")
    with open("datos.csv", "r") as archivo:
        lector_dict = csv.DictReader(archivo)
        datos_ordenados = sorted(lector_dict, key=lambda row: int(row["Edad"]))
    
    with open("datos_ordenados.csv", "w", newline="") as archivo:
        campos = ["Nombre", "Edad", "Ciudad"]
        escritor_dict = csv.DictWriter(archivo, fieldnames=campos)
        escritor_dict.writeheader()
        escritor_dict.writerows(datos_ordenados)
        
    # Sección 11: Manejo de Archivos
    print()
    print("11. Manejo de Archivos")
    # Escritura en un archivo
    with open("archivo.txt", "w", encoding="utf-8") as f:
        f.write("Hola, mundo!\n")
        f.write("Otra línea de texto.\n")
    
    # Lectura de un archivo
    with open("archivo.txt", "r", encoding="utf-8") as f:
        contenido = f.read()
        print(contenido)
    
    # Lectura línea por línea
    with open("archivo.txt", "r", encoding="utf-8") as f:
        for linea in f:
            print(linea.strip())
    
if __name__ == "__main__":
    main()
