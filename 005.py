#EJERCICIO1

# with open("datos.txt", "w") as file:
#     file.write("Nombre: Juan\n")
#     file.write("Edad: 31\n")
#     file.write("Ciudad: Madrid\n")


# with open("datos.txt") as file:
#     print("Contenido Inicial del archivo:")
#     for line in file:
#         print(line, end="")

# with open("datos.txt", "a") as file:
#     file.write("Ocupacion: Desarrollador\n")

# with open("datos.txt") as file:
#     print("\n\nContenido actualizado del archivo")
#     for line in file: 
#         print(line, end="")

#EJERCICIO2

# def leer_archivo(nombreArchivo):
    
#     try:
#         with open(nombreArchivo) as file:
#             print("Contenido Inicial del archivo:")
#             for line in file:
#                 print(line, end="")
#         pass
#     except FileNotFoundError:
#         print("Archivo no encontrado")
#     except Exception as e:
#         print("Ocurrió un error", e)

# leer_archivo("datos.txt")

#EJERCICIO3

class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre=nombre
        self.edad=edad
        self.ciudad=ciudad
    
    def saludar(self):
        print(f"Hola {self.nombre} ¿como estas?")

persona1= Persona("Miguel Ángel", 21, "Barranquilla")

persona1.saludar()

#EJERCICIO4

class Empleado(Persona):
    def __init__(self, nombre, edad, ciudad, ocupacion):
        super().__init__(nombre, edad, ciudad)
        self.ocupacion=ocupacion
    
    def saludar(self):
        print(f"Hola {self.nombre} ¿como estas? Que interesante que seas {self.ocupacion}")


empleado1= Empleado("Carlos", 16, "Barranquilla", "Futbolista")
empleado1.saludar()

