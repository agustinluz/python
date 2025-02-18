import random

def mostrar_imagen(intentos):
    """Muestra la imagen del ahorcado según los intentos restantes."""
    imagenes = [
        """
           ------
           |    |
                |
                |
                |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
                |
                |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
           |    |
                |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
          /|    |
                |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
          /|\\  |
                |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
          /|\\  |
          /     |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
          /|\\  |
          / \\  |
                |
        ---------
        """
    ]
    print(imagenes[6 - intentos])

def menu():
    opciones = ["1", "2", "3", "4"]
    while True:
        print("\nMenú")
        print("1. Introducir palabras en el fichero")
        print("2. Introducir nombre del jugador")
        print("3. Jugar")
        print("4. Salir")
        opcion = input("Elija una opción: ")
        if opcion in opciones:
            return opcion
        print("Opción no válida. Inténtalo de nuevo.")

def introducir_palabras():
    palabra = input("Escribe una palabra a introducir en el fichero: ").strip().lower()
    if palabra:
        with open("palabras.csv", encoding="utf-8", mode="a") as f:
            f.write(palabra + "\n")
        print("Palabra introducida correctamente.")
    else:
        print("No has introducido una palabra válida.")

def introducir_nombre():
    global nombre
    while True:
        nombre = input("Escribe tu nombre: ").strip()
        if nombre:
            print(f"Hola {nombre}, bienvenido al juego del ahorcado!")
            return
        print("Debes introducir un nombre válido.")

def jugar():

    with open("palabras.csv", encoding="utf-8", mode="r") as f:
        palabras = [line.strip() for line in f]

    palabra = random.choice(palabras)
    intentos = 6
    palabra_oculta = ["_" for _ in palabra]
    letras_incorrectas = []

    print("\n¡Comienza el juego!")
    while intentos > 0:
        print("\n" + " ".join(palabra_oculta))
        print(f"Letras incorrectas: {', '.join(letras_incorrectas) if letras_incorrectas else 'Ninguna'}")
        print(f"Intentos restantes: {intentos}")
        mostrar_imagen(intentos)

        letra = input("Escribe una letra: ").strip().lower()
        
        if not letra or len(letra) > 1:
            print("Introduce una única letra válida.")
            

        if letra in letras_incorrectas or letra in palabra_oculta:
            print("Ya has intentado esa letra antes. Intenta con una diferente.")

        if letra in palabra:
            for i, caracter in enumerate(palabra):
                if caracter == letra:
                    palabra_oculta[i] = letra
        else:
            if letra not in letras_incorrectas:                
                letras_incorrectas.append(letra)
                intentos -= 1

        if "_" not in palabra_oculta:
            puntuacion = [150, 100, 75, 50, 25, 10][6 - intentos]
            print("\n¡HAS GANADO!")
            print(f"{nombre}, tu puntuación es: {puntuacion} puntos.")
            return

    print(f"\n{nombre}, has perdido. La palabra correcta era: {palabra}.")

def juego():
    global nombre
    nombre = ""
    while True:
        opcion = menu()
        if opcion == "1":
            introducir_palabras()
        elif opcion == "2":
            introducir_nombre()
        elif opcion == "3":
            if not nombre:
                print("Primero debes introducir tu nombre.")
            else:
                jugar()
        elif opcion == "4":
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    juego()
