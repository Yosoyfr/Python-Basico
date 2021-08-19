# Clase Persona
class Person:
    # Funcion init
    def __init__(self, fname, lname):
        self.firstname = fname  # Atributos
        self.lastname = lname  # Atributos

    # Metodos de la clase Person
    def printname(self):  # Imprime su nombre
        print(self.firstname, self.lastname)

    def presentation(self):  # Presentacion
        print("Hello, my name is", self.firstname)


# Instancia de un objeto de clase Persona
x = Person("Francisco", "Suarez")
x.printname()
x.presentation()

# Crear una clase secundaria


class Student(Person):
    pass  # palabra reservada que funciona cuando no deseo agregar mas atributos o metodos


y = Student("Luis", "Suarez")
y.printname()

# Crear una clase secundaria con otros atributos


class Student(Person):
    # palabra reservada que funciona cuando no deseo agregar mas atributos o metodos
    identityCard = 201807190


y = Student("Luis", "Suarez")
y.printname()
print(y.identityCard)


# Agregando la funcion _init_()
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


y = Student("Heather", "Paz")
y.printname()

# Agregando la función _init_() con la funcion super()


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


# Agregando nuevas propiedades y metodos
class Student(Person):
    def __init__(self, fname, lname, identityCard, graduationyear):
        super().__init__(fname, lname)
        self.identityCard = identityCard
        self.graduationyear = graduationyear

    def presentation(self):
        print("Hola yo soy", self.firstname, self.lastname,
              "con el carnet", self.identityCard)


student = Student("Francisco", "Suarez", 201807190, 2021)
student.presentation()
