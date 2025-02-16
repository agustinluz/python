#Desarrollar un programa en Python que simule un juego de lotería con un menú de opciones. 
#El programa debe permitir: 
#Añadir jugadores
#Generar una combinación ganadora
#Mostrar los jugadores con sus números
#Mostrar los ganadores
#Ordenar el fichero por el apellido
#Salir
#El programa debe solicitar por teclado el nombre y apellido , generar aleatoriamente siete números para cada jugador y almacenarlos en un fichero .csv. 
#La estructura será: 
#nombre,apellido1,num1,num2,num3,num4,num5,num6,num7
#Se debe generar la combinación ganadora antes de ver los ganadores. 
#El programa debe generar una combinación ganadora de 6 números, mostrar los nombres de los jugadores y sus números , e indicar si algún jugador ha ganado un premio. 
#Los premios se otorgan según la cantidad de números acertados.
#Premios:
#2 números acertados: 1.000 euros
#3 números acertados: 8.000 euros.
#4 números acertados: 20.000 euros.
#5 números acertados: 150.000 euros.
#6 números acertados: 1.000.000 euros.
import csv
import random 
def menu():
    print("1. Añadir jugador")
    print("2. Generar combinación ganadora")
    print("3. Mostrar jugadores con sus números")
    print("4. Mostrar ganadores")
    print("5. Ordenar el fichero por el apellido")
    print("6. Salir")
    opcion = int(input("Elija una opción: "))
    return opcion

def generarNumero():
    return random.randint(1, 49)

def generarCombinacionGanadora():
    return sorted([generarNumero() for i in range(6)])

def addJugador():
    nombre= input("Escribe el nombre del jugador")
    apellido= input("Escribe el apellido del jugador")
    numeros = [generarNumero() for i in range(7)]
    numeros.sort()
    return [nombre, apellido] + numeros
def mostrarJugadores():
    with open('datosprimitiva.csv', encoding="UTF-8", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def mostrarGanadores(combinacionGanadora):
    premios = {
        2: 1000,
        3: 8000,
        4: 20000,
        5: 150000,
        6: 1000000
    }
    
    with open('datosprimitiva.csv', encoding="UTF-8", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            nombre = row[0]
            apellido = row[1]
            numerosJugador = [int(num) for num in row[2:]]
            aciertos = 0
            for numero in numerosJugador:
                if numero in combinacionGanadora:
                    aciertos += 1
            if aciertos >= 2:
                print(f"{nombre} {apellido} ha acertado {aciertos} números y ha ganado {premios[aciertos]} euros.")


def ordenarPorApellido():
    with open('datosprimitiva.csv', encoding="UTF-8", mode="r") as file:
        reader = list(csv.reader(file))
    
    #reader.sort(key=lambda row: row[1]) Es otra manera de hacer que se ordende por uno de los datos del csv

#Este es el método de la burbuja
    n = len(reader)
    for i in range(n):
        for j in range(0, n - i - 1):
            if reader[j][1] > reader[j + 1][1]:
                # Intercambiar las filas si están en el orden incorrecto
                reader[j], reader[j + 1] = reader[j + 1], reader[j]
    
    with open('datosprimitiva_ordenado.csv', encoding="UTF-8", mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(reader)
    
    for i in range(n):
        print(reader[i])
    
    print("El fichero ha sido ordenado por apellido y guardado como 'datosprimitiva_ordenado.csv'.")

def main():
    while True:
        opcion = menu()
        if opcion == 1:
            jugador = addJugador()
            with open('datosprimitiva.csv', encoding="UTF-8", mode="a", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(jugador)
        elif opcion == 2:
            combinacionGanadora = generarCombinacionGanadora()
            print(f"Combinación ganadora: {combinacionGanadora}")
        elif opcion == 3:
            mostrarJugadores()
        elif opcion == 4:
            mostrarGanadores(combinacionGanadora)
        elif opcion == 5:
            ordenarPorApellido()
        elif opcion == 6:
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")
    
    
    print("Gracias por utilizar el programa. Hasta pronto!")

if __name__ == "__main__":
    main()