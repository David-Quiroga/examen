from jefe           import Jefe
from jefe           import Secretaria
from empleado       import Empleado
from practicante    import Practicante

class Empresa:
    nombreEmpresa       = str
    jefe                = Jefe("", "", "", "")
    empleado            = Empleado("", "", "")
    practicante         = Practicante("", "", "", "", "")
    
    def __init__(self, nombreEmpresa, jefe, empleado, practicante):
        self.nombreEmpresa      = nombreEmpresa
        self.jefe               = jefe
        self.empleado           = empleado
        self.practicante        = practicante
        
