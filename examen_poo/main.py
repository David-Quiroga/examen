#El presente examen es Teórico Practico ante lo cual se les solicita leer detenidamente las preguntas y realizar un ejemplo usando PYTHON en el que se demuestre : 

#CREACION DE UNA CLASE QUE CONTENGA UN METODO Y SU OBJETO IMPRESO EJECUTANDO EL METODO __str__
#CREACION DE UNA CLASE QUE CONTENGA UN METODO Y SU OBJETO IMPRESO EJECUTANDO EL METODO.
#REALIZAR UNA HERENCIA DENTRO DEL MISMO ARCHIVO DE UNA DE LAS CLASES CREADAS, CREANDO UN METODO STR EN EL HIJO (IMPRMIR UN OBJETO CON ESA CLASE)
#REALIZAR UNA HERENCIA ENTRE ARCHIVOS CREANDO UN METODO EN EL HIJO
#REALIZAR UNA HERENCIA EN UNA CLASE QUE CONTENGA VARIOS OBJETOS (2) Y OBJETOS DENTRO DE OBJETOS (2)
#REALIZAR UNA HERENCIA QUE CONTENGA: VARIOS OBJETOS (2), OBJETOS DENTRO DE OBEJTOS (2) Y OBJETOS DENTRO DE OBJETOS DENTRO DE OBJETOS (2)

from jefe        import Jefe
from jefe        import Secretaria
from empleado    import Empleado
from practicante import Practicante
from empresa     import Empresa



if __name__ == "__main__":
    print("**JEFE**")

    jef1    = Jefe("Paolo", "Londra", 31, "Ingeniero")
    jef2    = Jefe("Agustin", "Suarez", 51, "Full Stack")
    sec1    = Secretaria("Maria", "Suarez", 41, "Bombero", "Nocturna", True, 41)
    sec2    = Secretaria("Agustina", "Fernandez", 31, "Developer", "Matutina", False, 21)


    print(vars(jef1))
    print(vars(jef2))
    
    print("**EMPLEADO**")
    emp1    = Empleado("Julio", 1, "RRHH")
    emp2    = Empleado("Bart", 2, "Marketing")
    print(vars(emp1))
    print(vars(emp2))
    
    print("**PASANTE**")
    
    pas1    = Practicante("Antonio", 3, "RRHH", "Yavirac", "Segundo")
    pas2    = Practicante("Fernando", 4, "Limpieza", "UDLA", "Tercer")

    print(vars(pas1))
    print(vars(pas2))
    
    print("**Metodo con STR**")
    print(sec1)
    print(sec2)
    
    
    print("**OBJETO DENTRO DE OTRO OBJETO**")
    empre1  = Empresa("Linkearte", jef1, emp1, pas1 )
    print(vars(empre1))
    print(vars(jef1))
    print(vars(emp1))
    print(vars(sec1))

    empre2  = Empresa("Sociedad Astronomica", jef2, emp2, pas2 )
    print(vars(empre1))
    print(vars(jef2))
    print(vars(emp2))
    print(vars(sec2))
    