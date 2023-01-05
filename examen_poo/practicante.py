from empleado import Empleado

class Practicante(Empleado):
    universidad     = str
    semestre        = str
    
    def __init__(self, nombre, idEmpleado, departamento, universidad, semestre):
        super().__init__(nombre, idEmpleado, departamento)
        self.universidad    = universidad
        self.semestre       = semestre
        
    def otropasante(self, otropasante):
        return f"Este pasante trabaja en el departamento de {self.departamento}. Ademas viene de la universidad de {self.universidad}, y su semestre es {self.semestre}. Su noombre es {otropasante.nombre}"