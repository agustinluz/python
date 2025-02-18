import random
import time

# Lista de imágenes del ahorcado
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
          /|\   |
                |
                |
        ---------
        ''',
        '''
           ------
           |    |
           O    |
          /|\   |
          /     |
                |
        ---------
        ''',
        '''
           ------
           |    |
           O    |
          /|\   |
          / \   |
                |
        ---------
        '''
    ]
    print(imagenes[6 - intentos])

def menu():
    print("\nMenú")
    print("1. Introducir palabras en el fichero")
    print("2. Introducir nombre del jugador")
    print("3. Jugar")
    print("4. Salir")
    return int(input("Elija una opción: "))

def introducir_palabras():
    with open("palabras.csv", encoding="utf-8", mode="a") as f:
        palabra = input("Escribe una palabra a introducir en el fichero: ").strip().lower()
        if palabra:
            f.write(palabra + "\n")
            print("Palabra introducida correctamente.")
        else:
            print("No se puede introducir una palabra vacía.")

def introducir_nombre():
    global nombre
    nombre = input("Escribe tu nombre: ").strip()
    print(f"Hola {nombre}, bienvenido al juego del ahorcado!")

def jugar():
    try:
        with open("palabras.csv", encoding="utf-8", mode="r") as f:
            palabras = f.readlines()
            if not palabras:
                print("No hay palabras en el fichero. Agrega algunas antes de jugar.")
                return
            
            palabra = random.choice(palabras).strip()
            intentos = 6
            palabra_oculta = ["_" for _ in palabra]
            letras_incorrectas = []
            puntuacion = 0

            print("\n¡Comienza el juego!")
            start_time = time.time()
            
            while intentos > 0:
                print(" ".join(palabra_oculta))
                print(f"Letras incorrectas: {', '.join(letras_incorrectas)}")
                print(f"Intentos restantes: {intentos}")
                mostrar_imagen(intentos)
                
                letra = input("Escribe una letra: ").lower()
                
                if len(letra) != 1 or not letra.isalpha():
                    print("Por favor, introduce solo una letra válida.")
                    continue
                
                if letra in letras_incorrectas or letra in palabra_oculta:
                    print("Ya has intentado esa letra antes. Intenta con otra.")
                    continue

                if letra not in palabra:
                    letras_incorrectas.append(letra)
                    intentos -= 1
                else:
                    for i in range(len(palabra)):
                        if palabra[i] == letra:
                            palabra_oculta[i] = letra
                
                if "_" not in palabra_oculta:
                    print("\n¡HAS GANADO!")
                    tiempo = int(time.time() - start_time)
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
                    print(f"{nombre} ha obtenido {puntuacion} puntos.")
                    return
            
            print(f"\nHas perdido. La palabra correcta era: {palabra}.")
            print(f"{nombre} ha obtenido {puntuacion} puntos.")
    except FileNotFoundError:
        print("El archivo 'palabras.csv' no existe. Por favor, agrega palabras primero.")

def juego():
    global nombre
    nombre = ""
    while True:
        try:
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
            else:
                print("Opción incorrecta. Inténtalo de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Ejecutar el juego
juego()
