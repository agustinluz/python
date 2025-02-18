print ("**********************************")
print ("Ejemplo 1: Listas dentro de tuplas")
print ("**********************************")

tupla_con_listas = ([1, 2, 3], [4, 5, 6], [7, 8, 9]) 	#una tupla con tres listas
elemento = tupla_con_listas[1][1]  			            #Accedo al 2º elemento de la 2ª lista 
print("Elemento accedido:", elemento)		            #Elemento accedido: 5
tupla_con_listas[0][2] = 10				                #Modifico el 3º elemento de la 1ª lista 
print("Tupla después de la modificación:", tupla_con_listas)

print ("**********************************")
print ("Ejemplo 2: Tupla con diccionarios")
print ("**********************************")

tupla_con_diccionarios = ({"nombre": "Alice", "edad": 30}, {"nombre": "Bob", "edad": 25}) #Defino una tupla con dos diccionarios
nombre = tupla_con_diccionarios[0]["nombre"]                    #Accedo al valor asociado a la clave ‘nombre’ del  1ª diccionario 
print("Nombre accedido:", nombre)	                            #Nombre accedido: Alice
tupla_con_diccionarios[1]["edad"] = 26 	                        #Modifico el valor asociado a la clave ‘edad’ del  2ª diccionario 
print("Tupla después de la modificación:", tupla_con_diccionarios)

print ("**********************************")
print ("Ejemplo 3: Listas con diccionarios")
print ("**********************************")

lista_con_diccionarios = [{"ciudad": "Sevilla", "pais": "España"}, {"ciudad": "Lisboa", "pais": "Portugal"}] 		
#Defino una lista con dos diccionarios
ciudad = lista_con_diccionarios[1]["ciudad"] 		#Accedo al valor asociado a la clave ‘ciudad’ del  2ª diccionario 
print("Ciudad accedida:", ciudad)		            #Ciudad accedida: Lisboa
lista_con_diccionarios[0]["pais"] = "Estados Unidos"        #Modifico el valor asociado a la clave ‘pais’ del  1ª diccionario 
print("Lista después de la modificación:", lista_con_diccionarios)

print ("**********************************")
print ("Ejemplo 4: Conjunto con Tuplas")
print ("**********************************")

conjunto_con_tuplas = {("kiwi", "verde"),("fresa", "rojasss"),  ("uva", "morado")} #Defino un conjunto  con varias tuplas
print ("conjunto_con_tuplas:", conjunto_con_tuplas)
lista_de_tuplas = list(conjunto_con_tuplas) 	    #Convierto el conjunto en lista para acceder a los elementos
print ("lista_de_tuplas:", lista_de_tuplas)
fruta_color = lista_de_tuplas[0][1]  		        #Accedo al 2º elemento de la 1ª tupla
print("Color accedido:", fruta_color)		        #Color accedido: XXX
# Resultado: depende del orden, podría ser "roja", "amarillo" o "morado"
