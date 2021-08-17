# La funcion print de Python se usa a menudo para imprimir variables.
print("Hola")

# Python no tiene ningún comando para declarar una variable.
mivariable = 0
x = 5.10
y = "Hello, World!"
x1 = 5
y2 = "Francisco"

# Las variables no necesitan declararse con ningún tipo en particular e incluso pueden cambiar de tipo después de que se hayan establecido.
x = 5  # x es de tipo int
x = "Francisco"  # x es ahora de tipo str

# Las variables de cadena se pueden declarar utilizando comillas simples o dobles:
x = "Francisco"
# es igaul a
x = 'Francisco'


# Ejemplo de identificadores para variables legales
name_2 = "Francisco"
Name = "Luis"
NAME = "Paula"
_name = "Allen"
age = 21
height = 1.83

print(name_2)
print(_name)
print(Name)
print(NAME)

# Identificadores para variables ilegales:
'''
2myvar = "Francisco"
my-var = "Francisco"
my var = "Francisco"
'''

# Asignar valor a múltiples variables
# Python le permite asignar valores a múltiples variables en una línea:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# Y puede asignar el mismo valor a múltiples variables en una línea:
x = y = z = "Orange"
print(x)
print(y)
print(z)


# Para combinar texto y una variable, Python usa el + carácter:
x = "awesome"
y = "!!!"
print("Python is " + x + y)

# Para los números, el + carácter funciona como operador matemático:
x = 5
y = 10
print(x + y)


'''
#Si intenta combinar una cadena y un número, Python le dará un error:
x = 5
y = "Francisco"
print(x + y)
'''
# Para combinar texto y Enteros en variables, Python usa el carácter: ' , '
x = 5
y = "Francisco tiene:"
z = "años"
print(y, x, z)

# Otra forma es la siguiente

x = 5
y = "Francisco tiene:"
z = "años"
result = y + " " + str(x) + " " + z
print(result)
