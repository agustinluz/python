import random

def mostrar_imagen(intentos):
    imagenes = [
        '''
           ------
           |    |
                |
                |
                |
                |
        ---------
        ''',
        '''
           ------
           |    |
           O    |
                |
                |
                |
        ---------
        ''',
        '''
           ------
           |    |
           O    |
           |    |
                |
                |
        ---------
        ''',
        '''
           ------
           |    |
           O    |
          /|    |
                |
                |
        ---------
        ''',
        '''
           ------
           |    |
           O    |
          /|\\  |
                |
                |
        ---------
        ''',
        '''
           ------
           |    |
           O    |
          /|\\  |
          /     |
                |
        ---------
        ''',
        '''
           ------
           |    |
           O    |
          /|\\  |
          / \\  |
                |
        ---------
        '''
    ]
    print(imagenes[6 - intentos])

def menu():
    print("Menú")
    print("1. Introducir palabras en el fichero")
    print("2. Introducir nombre del jugador")
    print("3. Jugar")
    print("4. Salir")
    return int(input("Elija una opción: "))

def introducir_palabras():
    with open("palabras.csv", encoding="utf-8", mode="a") as f:
        palabra = input("Escribe una palabra a introducir en el fichero: ")
        f.write(palabra + "\n")
        print("Palabra introducida correctamente.")

def introducir_nombre():
    global nombre
    nombre = input("Escribe tu nombre: ")
    print(f"Hola {nombre}, bienvenido al juego del ahorcado!")

def jugar():
        with open("palabras.csv", encoding="utf-8", mode="r") as f:
            palabras = f.readlines()
            if len(palabras) == 0:
                print("No hay palabras en el fichero. Añade algunas antes de jugar.")

            palabra = random.choice(palabras).strip()
            intentos = 6
            palabra_oculta = ["_" for _ in range(len(palabra))]
            letras_incorrectas = []
            puntuacion = 0

            print("Comienza el juego!")

            while intentos > 0:
                print(" ".join(palabra_oculta))
                print(f"Letras incorrectas: {', '.join(letras_incorrectas)}")
                print(f"Intentos restantes: {intentos}")
                mostrar_imagen(intentos)

                letra = input("Escribe una letra: ").lower()

                if letra in letras_incorrectas or letra in palabra_oculta:
                    print("Ya has intentado esa letra antes. Intenta con una diferente.")

                if letra not in palabra:
                    letras_incorrectas.append(letra)
                    intentos -= 1
                else:
                    for i in range(len(palabra)):
                        if palabra[i] == letra:
                            palabra_oculta[i] = letra

                if "_" not in palabra_oculta:
                    print("¡HAS GANADO!")
                    if intentos == 6:
                        puntuacion = 150
                    elif intentos == 5:
                        puntuacion = 100
                    elif intentos == 4:
                        puntuacion = 75
                    elif intentos == 3:
                        puntuacion = 50
                    elif intentos == 2:
                        puntuacion = 25
                    else:
                        puntuacion = 10

                    print(f"{nombre} tu puntuación es: {puntuacion} puntos.")
                    break

            if "_" in palabra_oculta:
                print(f"{nombre} has perdido. La palabra correcta era: {palabra}.")

def juego():
    global nombre
    nombre = ""
    while True:
        opc = menu()
        if opc == 1:
            introducir_palabras()
        elif opc == 2:
            introducir_nombre()
        elif opc == 3:
            if nombre == "":
                print("Primero debes introducir tu nombre.")
            else:
                jugar()
        elif opc == 4:
            print("¡Hasta luego!")
            break


juego()