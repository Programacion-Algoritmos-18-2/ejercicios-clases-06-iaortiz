import abc
#Clase abstracta equipo
class Persona_Equipo(metaclass = abc.ABCMeta):
    def __init__(self, nom):
        self.nombre = nom
    #Metodos get y set
    def agregar_nombre(self, nf):
        self.nombre = nf

    def obtener_nombre(self):
        return self.nombre
    #Metodo abstracto
    @abc.abstractmethod
    def entrenamiento(self):
        pass

#Clase fubtolista hija de Persona Equipo
class Futbolista(Persona_Equipo):
    def __init__(self, fu):
        super(Futbolista, self).__init__(fu)
        self.n_futbolista = ""

    # Metodos get y set
    def agregar_furbolista(self, fu):
        self.n_futbolista = fu

    def obtener_entrenador(self):
        return self.n_futbolista
    #Presentacion
    def entrenamiento(self):
        print("Yo %s , futbolista, hago practica en el entrenamiento" % (self.nombre))


#Clase fubtolista hija de Persona Equipo
class Entrenador(Persona_Equipo):
    def __init__(self, n_e):
        super(Entrenador, self).__init__(n_e)
        self.nombre_entrenador = ""

    # Metodos get y set
    def agregar_entrenador(self, ne):
        self.nombre_entrenador = ne

    def obtener_entrenador(self):
        return  self.nombre_entrenador
    #Presentacion
    def entrenamiento(self):
        print("Yo %s ,entrenador, soy el director del entrenamiento " % (self.nombre))

#Clase fubtolista hija de Persona Equipo
class Medico_equipo(Persona_Equipo):
    def __init__(self, me):
        super(Medico_equipo, self).__init__(me)
        self.titulo = ""

    # Metodos get y set
    def agregar_titulo(self, ti):
        self.titulo = ti

    def obtener_titulo(self):
        return  self.titulo
    #Presentacion
    def entrenamiento(self):
        print("Yo %s, atiendo a los jugadores en el entrenamiento." %(self.nombre))

#Clase fubtolista hija de Persona Equipo
class Presidente_Equipo(Persona_Equipo):
    def __init__(self, pro):
        super(Presidente_Equipo, self).__init__(pro)
        self.propiedades= 0
    # Metodos get y set
    def agregar_prop(self,pr):
        self.propiedades = pr

    def obtener_prop(self):
        return self.propiedades
    #Presentacion
    def entrenamiento(self):
        print("Yo %s, presidente, pongo el dinero para el entrenamiento. " % (self.nombre))