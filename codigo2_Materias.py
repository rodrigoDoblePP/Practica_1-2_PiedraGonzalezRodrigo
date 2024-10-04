#Codigo numero 2

print ("")
print("Piedra Gonzalez Rodrigo 3-W")
print (" ")

Materias = ["pensamiento matemático", "español" , "inglés" , "química" , "civismo" , "francés"]
#Defino Materias En forma de listas
print (Materias) #Imprimo la lista Materias
print(" ")
# 3.- Mostrar el mensaje "Estoy cursando <materia>" para cada una
for Materias in Materias:
    print(f"Estoy cursando {Materias}")
print (" ")
mate= (float(input("¿Que calificacion obtuviste en pensamiento matematico: "))) # Pedimos la calificacion de cada materia
esp= (float(input("¿Que calificacion obtuviste en español:  "))) # Pedimos la calificacion de cada materia
ing= (float(input("¿Que calificacion obtuviste en ingles: "))) # Pedimos la calificacion de cada materia
qui= (float(input("¿Que calificacion obtuviste en quimica: "))) # Pedimos la calificacion de cada materia
civ= (float(input("¿Que calificacion obtuviste en civismo:  "))) # Pedimos la calificacion de cada materia
fr= (float(input("¿Que calificacion obtuviste en frances:  "))) # Pedimos la calificacion de cada materia
print (" ")  #imprimimos espacio
print ("En Pensamiento matematico has obtenido :",mate) #imprimimos la calificacion introducida de cada materia
print ("En español has obtenido :",esp) #imprimimos la calificacion introducida de cada materia
print ("En ingles has obtenido :",ing) #imprimimos la calificacion introducida de cada materia
print ("En quimica has obtenido :",qui) #imprimimos la calificacion introducida de cada materia
print ("En civismo has obtenido :",civ) #imprimimos la calificacion introducida de cada materia
print ("En francés has obtenido :",fr) #imprimimos la calificacion introducida de cada materia