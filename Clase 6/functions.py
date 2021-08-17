# Creacion de una funcion
def my_function():
    print("Hola desde mi funcion")


# Llamada de una funcion
# my_function()


# Funcion que recibe un parametro
def saludar(nombre):
    print("Hola " + nombre + "!!")


# saludar("Francisco")
# saludar("Luis")
# saludar("Heather")

# Funcion que recibe dos parametros

def concatenarNombre(nombre, apellido):
    print(nombre, apellido)


# concatenarNombre("Francisco", "Suarez")

''' Error porque hace falta un argumento
def concatenarNombre(nombre, apellido):
    print(nombre, apellido)

concatenarNombre("Francisco")
'''

# Argumentos por palabra clave


def alumnos(z, y, x):
    print("Alumno x:", x)
    print("Alumno y:", y)
    print("Alumno z:", z)

# alumnos(x="Francisco", y="Luis", z="Heather")

# Return en funciones


def areaCuadrado(x):
    return x**2


def areaRectangulo(x, y):
    return x*y


def areaTringulo(b, h):
    return b*h/2


def areaCirculo(r):
    return 3.1416*r**2
