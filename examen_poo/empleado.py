class Empleado:
    nombre          = str
    idEmpleado      = int
    departamento    = str
    
    def __init__(self, nombre, idEmpleado, departamento):
        self.nombre         = nombre
        self.idEmpleado     = idEmpleado
        self.departamento   = departamento