from paquete_equipo.modelo1 import *
#p = Persona_Equipo()
f = Futbolista("Antonio")
e = Entrenador("Jose")
m = Medico_equipo("Ramon")
p = Presidente_Equipo("Francisco")
print("EJERCICIO 1")
lista = (f, e, m, p)
for l in lista:
    l.entrenamiento()