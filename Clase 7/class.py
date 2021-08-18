class MyClass:
    # Atributos (propiedades) de MyClass
    name = "My class"
    x = 10
    y = ["My", "Class"]

    # Operaciones(Metodos/Funciones) de MyClass
    def printName(name):
        print(name)

# Crear objeto
# MyClass c = new MyClass() ---  JAVA
# Todos los atributos y metodos los va tener (C)


# Declaracion de un objeto
myclass_ = MyClass()
print("El nombre de myclass es:", myclass_.name)

# Declaracion de un objeto
obj = MyClass()
# Asignacion de un valor a un objeto
obj.name = "Mi clase"
print("Mi nombre es:", obj.name)
