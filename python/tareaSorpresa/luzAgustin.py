lista=[ input(f"Escribe el nombre numero {i}") for i in range (5)]
def crearLista():
    lista3[53.2,141.8,105.3,78.2,60.4]
    return print(lista3)
def mediaYmas(lista3):
    maximo=max(lista3)
    minimo=min(lista3)
    media=sum(lista3)/len(lista3)
    return print(f"Media: {media}, maximo: {maximo}, minimo:{minimo}")
def eliminarUno(nombre):
    lista.pop(nombre)
def crearLista2(lista):
    lista2=lista
    return print(lista2)
def agregarLista2(nombre):
    lista2.append(nombre)
    return print(f"El contenido de la lista 1: {lista},\n contenido de la lista 2:{lista2}")


opc=0
lista2=[]
lista3=[]
while opc!=9:
    print("\nMenú de operaciones:")
    print("1: MOSTRAR LISTA")
    print("2: INSERTAR")
    print("3: ELIMINA UNO")
    print("4: CREAR COPIA")
    print("5: AÑADE UNO A LA 2 LISTA")
    print("6: CREAR TERCERA LISTA")
    print("7: MOSTRAR CONTENIDO, MEDIA PESO MAXIMO Y MINIMO")
    print("8: CALCULAR CUANTOS PESAN MAS DE 100KG")
    print("9: SALIR")

    opc=int(input("Elige una upcion del menu: "))

    match opc:
        case 1: 
            print(F"Contenido de la lista: {lista}")
        case 2:
            lista.append("Fernando")
            print("Añadido")
        case 3:
            nombreBuscar=input("Escribe el nombre a buscar y eliminar: ")
            eliminarUno(nombreBuscar)
        case 4:
            crearLista2(lista)
        case 5:
            nombreNuevo=input("Escribe el nombre que quieres agregar en la lista 2: ")
            agregarLista2(nombreNuevo)
        case 6:
            crearLista()
            print("SE HA CREADO UNA NUEVA LISTA (CREO)")
        case 7:
            mediaYmas(lista3)
        case 8:
            mas100 = [ i+1 for i in range(len(lista3)) if 100 >= lista3[i]]
            print(f"Los pesos que superan los 100 son:  {mas100}")
        case 9:
            print("SALIENDO")
        case _:
            print("Opción no válida. Inténtalo de nuevo.")