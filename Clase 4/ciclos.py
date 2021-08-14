# Ejemplos del FOR

estudiantes = ["Luis", "Andres", "Andy",
               "Angel", "Mateo", "Hector", "Sebastian"]

'''
for nombre in estudiantes:
    print(nombre)
'''


profesor = "Francisco"

'''
for letra in profesor:
    print(letra)
'''

estudiantes = ["Luis", "Andres", "Andy",
               "Angel", "Mateo", "Hector", "Sebastian"]

'''
for nombre in estudiantes:
    if nombre == "Angel":
        break
    print(nombre)
'''

estudiantes = ["Luis", "Andres", "Andy",
               "Angel", "Mateo", "Hector", "Sebastian"]

'''
for nombre in estudiantes:
    if nombre == "Angel":
        continue
    print(nombre)
'''


nombres = ["Luis", "Andres", "Andy",
           "Angel", "Mateo", "Hector", "Sebastian"]

apellidos = ["De Leon", "Peñate", "Monroy",
             "Torcelli", "Hernandez", "Chaclan", "Solares"]

for nombre in nombres:
    for apellido in apellidos:
        print(nombre, apellido)
