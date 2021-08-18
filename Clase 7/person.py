class Person:
    # self es equivalente a this en java
    def __init__(self, name, age):  # La funcion init es como el equivalente a un constructor en java
        self.name = name  # Atributo (propiedad)
        self.age = age  # Atributo (propiedad)

    # Operaciones(Metodos/Funciones) de Person
    def presentation(self):
        print("Hello my name is " + self.name)


p1 = Person("Francisco Suarez", 21)
p2 = Person("Heather Paz", 15)

# print("Nombre:", p1.name, "- Edad:", p1.age)
# print("Nombre:", p2.name, "- Edad:", p2.age)

p1.presentation()

# Modificacion de propiedades de un objeto
p1.name = "Luis Suarez"
p1.presentation()

# Eliminacion de propiedades de un objeto
del p1.age

# Eliminacion de un objeto
del p1
