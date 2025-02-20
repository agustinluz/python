import random 

def imagenes (imga):
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
    imagen=len(imagenes)-imga
    return imagenes[imagen]

def menu():
    print("Escoge una de las opciones")
    print("1.Introducir palabras en el fichero ")
    print("2.Introducir nombre del jugador")
    print("3.Jugar")
    print("4. Mostrar ranking")
    print("5. Salir")
    opcion =int(input("Elige una opción: "))
    return opcion

def escribirPalabra():
    palabra=input("Escribe la palabra a introducir: ").strip().lower()
    if palabra : 
        with open ("./palabras.csv", encoding="UTF-8", mode="a", newline="\n" ) as f:
            f.write(palabra + "\n")
        print("La palabra se ha escrito correctamente ")
    else:
        print("No se ha introducido una palabra de manera adecuada")

def escribeJugador():
    global jugadores, jugador 
    jugadores = []
    jugador  = {
        "nombre": input("Escribe el nombre del jugador: "),
        "intentos": 6,
        "puntos": 0
    }
    jugadores.append(jugador)
    print("Jugador añadido:", jugador)

def jugar():
    with open ("./palabras.csv", encoding="UTF-8", mode="r") as F:
        palabras=[line.strip() for line in F]
    
    
    
    palabra=random.choice(palabras)
    intentos=6
    palabraOculta=["_" for _ in palabra]
    letraIncorrecta=[]
    
    while intentos > 0:
        
        print(imagenes(intentos))
        print(" ".join(palabraOculta))
        print(f"\nTienes {intentos} intentos")
        print(f"\nLetras incorrectas: {','.join(letraIncorrecta) if letraIncorrecta else 'Na de na'}")
        
        letra=input("Escribe una letra: ").strip().lower()
        
        if letra in palabra:
            for i, caracter in enumerate(palabra):
                if caracter == letra:
                    palabraOculta[i] = letra 
        else:
            if letra not in letraIncorrecta:
                letraIncorrecta.append(letra)
                intentos-=1
            else:
                print("Ya has intentado esta letra antes")
        
        if "_" not in palabraOculta:
            puntuacion = [150, 100, 75, 50, 25, 10][6 - intentos]
            jugador["puntos"]=puntuacion
            print(f"HAS GANADO!!!!, {jugador['nombre']} su puntuacion es : {puntuacion} puntos")
            break
    if "_" in palabraOculta:
        print(f"\n{jugador['nombre']}, has perdido. La palabra correcta era: {palabra}.")

def mostrar_ranking():
    if not jugadores:
        print("No hay jugadores registrados.")
        return

    mejor_jugador = max(jugadores, key=lambda j: j["puntos"])
    
    print("\n🏆 RANKING DE JUGADORES 🏆")
    for jugador in sorted(jugadores, key=lambda j: j["puntos"], reverse=True):
        print(f"{jugador['nombre']} - {jugador['puntos']} puntos")

    print(f"\n🎉 El mejor jugador es {mejor_jugador['nombre']} con {mejor_jugador['puntos']} puntos")

def juego():
    while True:
        opc=menu()
        match opc:
            case 1 :
                escribirPalabra()
            case 2:
                escribeJugador()
            case 3:
                if not jugador:
                    print("Escribe un nombre antes burrico")
                else:
                    jugar()
            case 4:
                mostrar_ranking()
            case 5:
                break
            case _ :
                print("no has introducido una opcion correcta")

if __name__ == "__main__":
    juego()