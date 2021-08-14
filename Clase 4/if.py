# Ejemplos de IF

if 2 == 1:
    print("Esto es verdadero")


x = 22
y = 20

if x <= y:
    print("Y es mayor o igual que X")


tengoCovid = False

if tengoCovid:
    print("No salir de casa")

# Ejemplos de elif

x = 22
y = 20

'''
if x < y:
    print("Y es mayor que X")
elif x == y:
    print("Y es igual a X")
elif x > y:
    print("Y es menor que X")
elif x != y:
    print("Y no es igual a X")
'''

# Ejemplos de else

x = 22
y = 21
'''
if x < y:
    print("Y es mayor que X")
elif x > y:
    print("Y es menor que X")
else:
    print("Y es igual X")
'''

tengoCovid = False
'''
if tengoCovid:
    print("No salir de casa")
else:
    print("Debo cuidarme")
'''

# Ejemplo de AND
x = 20
y = 20
z = 21

'''
EL AND FUNCIONA COMO LA MULTIPLICACION
0*0 = 0
0*1 = 0
1*0 = 0
1*1 = 1 
'''
'''
if x == y and x != z:
    print("Esto se cumple")
else:
    print("No se cumple")
'''

# Ejemplo de OR

x = 20
y = 20
z = 21

'''
EL OR FUNCIONA COMO LA SUMA
0+0 = 0
0+1 = 1
1+0 = 1
1+1 = 1
'''

'''
if x == y or x != z:
    print("Esto se cumple")
else:
    print("No se cumple")
'''

# IF ANIDADDOS

tengoCovid = False
tengoFiebre = False
grados = 33

if tengoCovid:
    print("No salir de casa")
    if tengoFiebre:
        print("Guardar reposo")
        if grados > 37:
            print("Tomar Ibuprofeno")
    else:
        print("Cuidar tu temperatura")
else:
    print("Debo cuidarme")
    if tengoFiebre:
        print("Probablemente sean sintomas de covid")
        if grados > 37:
            print("Tomar Ibuprofeno")
    else:
        print("Sigue cuidandote")
