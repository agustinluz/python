def menu():
    print("\n--- Menú de Gestión de Diccionario ---")
    print("1. Añadir un nuevo par clave-valor")
    print("2. Listar todas las claves y sus valores")
    print("3. Eliminar una clave y su valor asociado")
    print("4. Buscar el valor de una clave específica")
    print("5. Listar todas las claves del diccionario")
    print("6. Listar todos los valores del diccionario")
    print("7. Listar todos los pares clave-valor del diccionario")
    print("8. Comprobar si una clave existe en el diccionario")
    print("9. Calcular la suma de todos los valores del diccionario")
    print("10. Obtener la clave máxima y mínima del diccionario")
    print("11. Obtener el número total de elementos en el diccionario")
    print("12. Salir")

def main():
    diccionario = {}

    while True:
        menu()
        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("Error: Por favor ingresa un número válido.")
            continue

        if opcion == 1:
            clave = input("Escribe la clave: ")
            
            # Verificar si la clave ya existe
            if clave in diccionario:
                confirmar = input(f"La clave '{clave}' ya existe. ¿Deseas sobrescribirla? (s/n): ").lower()
                if confirmar != 's':
                    print("Operación cancelada.")
                    continue
            
            try:
                valor = int(input("Escribe el valor numérico: "))
            except ValueError:
                print("Error: El valor debe ser un número entero.")
                continue
                
            diccionario[clave] = valor
            print(f"Se ha añadido {clave} -> {valor}")

        elif opcion == 2:
            if not diccionario:
                print("El diccionario está vacío.")
                continue
                
            print("\n--- Elementos del diccionario ---")
            for clave, valor in diccionario.items():
                print(f"Clave: {clave.ljust(15)} Valor: {valor}")

        elif opcion == 3:
            clave = input("Clave a eliminar: ")
            if clave in diccionario:
                del diccionario[clave]
                print(f"Clave '{clave}' eliminada correctamente.")
            else:
                print(f"Error: La clave '{clave}' no existe en el diccionario.")

        elif opcion == 4:
            clave = input("Clave a buscar: ")
            valor = diccionario.get(clave, None)
            if valor is not None:
                print(f"Valor de '{clave}': {valor}")
            else:
                print(f"Error: La clave '{clave}' no existe en el diccionario.")

        elif opcion == 5:
            print("\n--- Claves del diccionario ---")
            print(list(diccionario.keys()) or "El diccionario está vacío.")

        elif opcion == 6:
            print("\n--- Valores del diccionario ---")
            print(list(diccionario.values()) or "El diccionario está vacío.")

        elif opcion == 7:
            print("\n--- Pares clave-valor ---")
            print(list(diccionario.items()) or "El diccionario está vacío.")

        elif opcion == 8:
            clave = input("Clave a verificar: ")
            existe = "existe" if clave in diccionario else "no existe"
            print(f"La clave '{clave}' {existe} en el diccionario.")

        elif opcion == 9:
            if diccionario:
                print(f"Suma total de valores: {sum(diccionario.values())}")
            else:
                print("El diccionario está vacío.")

        elif opcion == 10:
            if diccionario:
                try:
                    max_clave = max(diccionario)
                    min_clave = min(diccionario)
                    print(f"Clave máxima: {max_clave} - Clave mínima: {min_clave}")
                except TypeError:
                    print("Error: Las claves no son comparables entre sí.")
            else:
                print("El diccionario está vacío.")

        elif opcion == 11:
            print(f"Total de elementos: {len(diccionario)}")

        elif opcion == 12:
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

        # Pequeña pausa para visualizar resultados
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()