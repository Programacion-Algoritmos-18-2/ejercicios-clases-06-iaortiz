from paquete_equipo.modelo1 import *
#Creacion de objetos y le agregamos el nombre
f = Futbolista("Antonio")
e = Entrenador("Jose")
m = Medico_equipo("Ramon")
p = Presidente_Equipo("Francisco")
#Presentacion
print("EJERCICIO 1")
#Ciclo for para recorrer la lista de los objetos
lista = (f, e, m, p)
for l in lista:
    #Presentacion de cada uno de los entrenamientos de cada objeto
    l.entrenamiento()