### CLASES ###

# class MyClass:
#     i=123

#     def f(self):
#         return "hello world"
    

# clase=MyClass()
# print(clase)
# print(clase.i, clase.f())

# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
    
# x = Complex(3.0, -4.5)
# print(x.r)
# print(x.i)
# print(x)


# class Dog:

#     kind="canine"

#     def __init__(self, name):
#         self.name=name

# d=Dog("Fido")
# e=Dog("Buddy")

# print(d.kind)
# print(e.kind)

# print(d.name)
# print(e.name)

# class Dog:

#     def __init__(self, name):
#         self.name=name
#         self.tricks=[]
    
#     def add_trick(self, trick):
#         self.tricks.append(trick)

# d=Dog("Fido")
# e=Dog("Buddy")
# d.add_trick("play dead")
# e.add_trick("roll over")

# print(d.tricks)
# print(e.tricks)

# class Warehouse:
#     purpose="storage"
#     region = "west"

# w1= Warehouse()
# print(w1.purpose, w1.region)

# w2=Warehouse()
# w2.region="east"
# print(w2.purpose, w2.region)


# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre=nombre
#         self.edad=edad   
    
#     def saludar(self):
#         return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años"


# persona1= Persona("Miguel Ángel", 21)

# print(persona1.saludar())


# class Bag:
#     def __init__(self):
#         self.data=[]
    
#     def add(self, x):
#         self.data.append(x)
    
#     def addtwice(self, x):
#         self.add(x)
#         self.add(x)

# bag1=Bag()

# print(bag1.add("lapicero"))
# print(bag1.addtwice("lapicero"))

# print(bag1.data)


# class Mapping: 
#     def __init__(self, iterable):
#         self.items_list = []
#         self.__update(iterable)
    
#     def update(self, iterable):
#         for item in iterable:
#             self.items_list.append(item)
    
#     __update = update

# class MappingSubclass(Mapping):
#     def update(self, keys, values):
#         for item in zip(keys, values):
#             self.items_list.append(item)

for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
mi_diccionario={'one':1, 'two':2}
for key in mi_diccionario.items():
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')