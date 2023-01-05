#REALIZAR UNA HERENCIA DENTRO DEL MISMO ARCHIVO DE UNA DE LAS CLASES CREADAS, CREANDO UN METODO STR EN EL HIJO (IMPRMIR UN OBJETO CON ESA CLASE)
class Jefe:
    nombre      = str
    apellido    = str
    edad        = int
    carrera     = str
    
    def __init__(self, nombre, apellido, edad, carrera):
        self.nombre     = nombre
        self.apellido   = apellido
        self.edad       = edad
        self.carrera    = carrera
    
class Secretaria(Jefe):
    jornada     = str
    disponible  = bool
    experiencia = int 
    
    def __init__(self, nombre, apellido, edad, carrera, jornada, disponible, experiencia):
        super().__init__(nombre, apellido, edad, carrera)
        self.jornada        = jornada
        self.disponible     = disponible
        self.experiencia    = experiencia
        
    def __str__(self):
        return f"La secretaria {self.nombre}, su edad es de {self.edad}, trabaja en el turno de {self.jornada}, asi que si esta disponible: {self.disponible}. Cuenta con una experiencia de {self.experiencia} años. Y su carrera es {self.carrera}"
    
    