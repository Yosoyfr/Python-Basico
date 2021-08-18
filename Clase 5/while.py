# Ejemplos de while

# While normal
i = 1
while i < 6:
    print(i)
    i += 1

# The break Statement
# Lo que hace es parar toda la iteracion del ciclo
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# The continue Statement
# Lo que hace es parar toda la iteracion en curso y luego continua con la siguiente
# si es que existe
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


# The else Statement
# Este se ejecuta cuando la condicion del WHILE no se cumple
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i es mayor que 6")

# Whiles anidados

i = 0
j = 0
while i < 3:
    while j < 3:
        print(i, j)
        j += 1
    i += 1
    j = 0
