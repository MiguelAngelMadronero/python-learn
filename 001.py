#Variables


my_variable = "My String variable"
print(my_variable)

int_variable = 5
print(int_variable)
print(type(int_variable))


bool_variable = False
print(bool_variable)

str_variable = str(int_variable)
print(str_variable)
print(type(str_variable))


#Concatenación de variables en un print

print(my_variable, str_variable, bool_variable)
print("este es el valor :", bool_variable)
print('Hello',',', 'World','!')

#Funciones del sistema

print(len(my_variable))


#Variables en una sola linea

name, surname, alias, age = "Brais", "Moure", "MoureDev", 35

print(alias, age, name)

#Inputs
"""
first_name = input("What is your name: ")
age = input("How aold are you? ")

print(first_name)
print(age)
"""


num1=22
num2=22
resultado = num1 // num2
print("el resultado es : ", resultado)

