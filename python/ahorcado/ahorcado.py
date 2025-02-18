import random


def menu():
    print("\nMenú")
    print("1. Introducir palabras en el fichero")
    print("2. Introducir nombre del jugador")
    print("3. Jugar")
    print("4. Salir")
    return int(input("Elija una opción: "))

def introducirpalabras():
    with open("palabras.csv", encoding="utf-8", mode="a") as f:
        palabra=input("Escribe una palabra a introducir en el fichero ")
        f.write(palabra)
        print("Palabra introducida correctamente")

def introducirnombre():
    nombre=input("Escribe tu nombre: ")
    print(f"Hola {nombre}, bienvenido al juego del ahorcado!")

# Función para jugar al ahorcado
def jugar():
    with open("palabras.csv", encoding="utf-8", mode="r") as f:
        palabras = f.readlines()
        palabra = random.choice(palabras).strip()
        intentos = 6
        palabraOculta=[ "_"for i in range(palabra)]
        letrasIncorrectas = []
        while intentos > 0:
            print(" ".join(palabraOculta))
            print(f"Letras incorrectas: {', '.join(letrasIncorrectas)}")
            print(f"Intentos restantes: {intentos}")
            letra=print("Escribe una letra: ")
            if letra not in palabra:
                letrasIncorrectas.append(letra)
                intentos -= 1
            else:
                for i in range(len(palabra)):
                    if palabra[i] == letra:
                        palabraOculta[i] = letra
                if "_" not in palabraOculta:
                    print("HAS GANADO")
def juego():
    global nombre
    nombre = ""
    while True:
        opc=menu()
        if opc==1:
            introducirpalabras()
        elif opc==2:
            introducirnombre()
        elif opc==3:
            jugar()
        elif opc==4:
            break
        

            

