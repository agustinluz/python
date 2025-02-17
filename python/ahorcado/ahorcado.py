
#Desarrollar en Python el juego del ahorcado. El cual es un juego de adivinar palabras. 
#Los jugadores deberán adivinar palabras seleccionadas aleatoriamente de un fichero, con un límite de 6 intentos. 
# El programa debe gestionar la puntuación de los jugadores y mostrar la imagen del ahorcado a medida que vayan cometiendo errores.
#Las palabras a acertar se generarán aleatoriamente y serán seleccionadas de un fichero (palabras.csv) que cada alumno creará. El fichero debe contener mínimo 20 palabras. 
#El programa debe presentar un menú con las siguientes opciones:
#Introducir palabras en el fichero: Permite al usuario agregar nuevas palabras al fichero palabras.csv.
#Introducir nombre del jugador: Solicita al usuario que ingrese su nombre para identificar al jugador.
#Jugar: Inicia el juego del ahorcado. Se seleccionará una palabra aleatoria del fichero, se mostrará la palabra oculta con guiones y se pedirá al jugador que adivine las letras.
#ejemplo:       _ _ _ _ _ 
#para la palabra movil
#Salir: Termina el programa.

#Reglas del Juego:
#El jugador deberá adivinar una letra a la vez.
#El programa mostrará las letras acertadas en su posición correspondiente en la palabra.
#Si la letra no está en la palabra, el programa mostrará un mensaje indicando que la letra no está y la añadirá a una lista de letras incorrectas.
#El programa no permitirá adivinar letras repetidas y mostrará una lista de letras ya introducidas.
#Intentos:
#El jugador tendrá un máximo de 6 intentos para adivinar la palabra.
#Cada intento fallido reducirá el número de intentos restantes.
#El programa mostrará el número de intentos restantes después de cada intento.
#Se mostrará la imagen del ahorcado a medida que el jugador cometa errores.
#Debe mostrarse la imagen del ahorcado a medida que vayas  no acertando las palabras. 



#Sistema de Puntuación:
#Se asignará una puntuación basada en la rapidez con la que el jugador adivine la palabra y el número de intentos utilizados.
#Si aciertas al intento 1 sumas  150 puntos
#Si aciertas al intento 2 sumas 100 puntos
#Si aciertas al intento 3 sumas  75 puntos 
#Si aciertas al intento 4 sumas  50 puntos
#Si aciertas al intento 5 sumas  25 puntos
#Si aciertas al intento 6 sumas 10 puntos
#Final del Juego:
#Has obtenido XX puntos. 
#La palabra correcta era XXXXX
#Fulanito es el actual ganador con XX puntos. 


import random


def menu():
    print("Menú")
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
        

            

