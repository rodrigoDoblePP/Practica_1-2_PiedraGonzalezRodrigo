#Codigo numero 5
print ("")
print("Piedra Gonzalez Rodrigo 3-W")
print (" ")



numeros = [] # Lista para almacenar los números ganadores

#Suponiendo que son 6 numeros de la suerte para la loteria, si no pedimos mas
numeros.append(int(input("Número 1: "))) # Pedimos los 6 números de la lotería, uno por uno
numeros.append(int(input("Número 2: "))) # Pedimos los 6 números de la lotería, uno por uno
numeros.append(int(input("Número 3: "))) # Pedimos los 6 números de la lotería, uno por uno
numeros.append(int(input("Número 4: "))) # Pedimos los 6 números de la lotería, uno por uno
numeros.append(int(input("Número 5: "))) # Pedimos los 6 números de la lotería, uno por uno
numeros.append(int(input("Número 6: "))) # Pedimos los 6 números de la lotería, uno por uno 

numeros.sort() # ordena la lista de forma ascendente por defecto.


print("Números ganadores ordenados:", numeros) # Mostrar los números ordenados aca bien bonitos

