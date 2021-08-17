# Ejemplos del FOR

''' - Java - C# - C++
for (int i=0; i < 10 ; i++){
  //declareaciones o bloques de codigo
}
'''

# Sintaxis
# for objetoiterativo in secuencia :
# declaraciones (ifs , fors , while , metodos o funciones)

# Pasos
# 1. for
# 2. variable que va manejar las iteraciones
# 3. secuencia a iterar o recorrer
# 4. el area declaracion, donde vamos a manejar cada elemento de la secuencio

# Ciclo FOR noraml
estudiantes = ["Luis", "Andres", "Andy",
               "Angel", "Mateo", "Hector", "Sebastian"]

'''
for nombre in estudiantes:
    print(nombre)
'''

# Ciclo FOR para una cadena
profesor = "Francisco"

'''
for letra in profesor:
    print(letra)
'''

# The break Statement
# Lo que hace es parar toda la iteracion del ciclo
estudiantes = ["Luis", "Andres", "Andy",
               "Angel", "Mateo", "Hector", "Sebastian"]

'''
for nombre in estudiantes:
    print(nombre)
    if nombre == "Angel":
        break
'''

'''
for nombre in estudiantes:
    if nombre == "Angel":
        break
    print(nombre)
'''

# The continue Statement
# Lo que hace es parar toda la iteracion en curso y luego continua con la siguiente
# si es que existe
estudiantes = ["Luis", "Andres", "Andy",
               "Angel", "Mateo", "Hector", "Sebastian"]

'''
for nombre in estudiantes:
    if nombre == "Angel":
        continue
    print(nombre)
'''

# The else Statement
# Lo que hace es ejecutar un bloque de codigo al finalizar la iteracion del ciclo
estudiantes = ["Luis", "Andres", "Andy",
               "Angel", "Mateo", "Hector", "Sebastian"]

for nombre in estudiantes:
    print(nombre)
else:
    print("Ciclo finalizado!")

# The range() Function
'''
# Itera la cantidad de veces que definamos en el rango empezando desde 0
for x in range(6):
    print(x)
'''

'''
# El primer parametro indica el limite inferior y el segundo el limite
# superior del rango
for x in range(5, 6):
    print(x)
'''
'''
# El primer parametro indica el limite inferior, el segundo el limite
# superior y el tercero el paso de la iteracion
for x in range(2, 30, 3):
    print(x)
'''


# Ciclos anidados
nombres = ["Luis", "Andres", "Andy",
           "Angel", "Mateo", "Hector", "Sebastian"]

apellidos = ["De Leon", "Peñate", "Monroy",
             "Torcelli", "Hernandez", "Chaclan", "Solares"]
'''
for nombre in nombres:
    for apellido in apellidos:
        print(nombre, apellido)
'''
