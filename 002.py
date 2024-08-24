#EJERCICIO 1
# num1=int(input("escribe el primer numero: "))
# num2=int(input("escribe el segundo numero: "))

# resultado=num1+num2

# print("el resultado de la suma es: ", resultado)

#EJERCICIO2

# nombre=input("ESCRIBA SU NOMBRE: ")

# print("Hola", nombre, "¿Cómo estás?")

#EJERCICIO3
# num= int(input("escriba el numero: "))

# if(num==0):
#     print("el numero es cero")
# elif(num%2==0):
#     print("el numero es par")
# else:
#     print("el numero es impar")

#EJERCICIO4
# i=1

# while(i<=100):
#     if(i%3==0 and i%5==0):
#         print("FizzBuzz")
#     elif(i%3==0):
#         print("Fizz")
#     elif(i%5==0):
#         print("Buzz")
#     else:
#         print(i)
        
#     i=i+1

#EJERCICIO5

# nota=int(input("escriba su nota: "))

# if nota>=6 and nota<=10:
#     print("Aprobado")
# elif nota<6 and nota>=0:
#     print("Desaprobado")
# else:
#     print("nota no válida")

#EJERCICIO6

# def es_primo(n):
    
#     candidatos=0
#     divisores=0
#     candidatos=n
#     while candidatos>0:
#         if n%candidatos==0:
#             divisores=divisores+1
            
#         candidatos=candidatos-1

#     if divisores==2:
#         print("es primo")
#     else:
#         print("no es primo")


# es_primo(61)

# def es_primo(n):    

#     if n<=1:
#         return False
    
    
#     divisores=0
    
#     for i in range(1, n+1):
#         if n % i == 0:
#             divisores+=1

#     if divisores==2:
#         return True
#     else:
#         return False


# n=11
# if es_primo(n):
#     print(f"{n} es primo")
# else:
#     print(f"{n} no es primo")

# es_primo(n)


#EJERCICIO7

# def factorial(n):
#     acumulador=1
#     for i in range(1, n+1):
#         acumulador=acumulador*i
        
#     return acumulador

# print(factorial(5))

#EJERCICIO8

# def contador_vocales(frase):
#     numVocales=0
#     contador=0
#     while contador<len(frase):
#         if frase[contador] == "a":
#             numVocales+=1
#         elif frase[contador] == "e":
#             numVocales+=1
#         elif frase[contador] == "i":
#             numVocales+=1
#         elif frase[contador] == "o":
#             numVocales+=1
#         elif frase[contador] == "u":
#             numVocales+=1
#         contador+=1

#     return numVocales

# print(contador_vocales("habia una vez"))

# def contador_vocales(frase):
#    frase=frase.lower()
#    numVocales=0
#    for cararacter in frase:
#         if cararacter in "aeiou":
#             numVocales+=1
        


#    return numVocales

         
         

# print(contador_vocales("habia una vez"))


### LISTAS ###

# numeros=[1,2,3,4,5]

# numeros.append(6)
# numeros.insert(0,0)
# numeros.pop(3)
# # numeros.sort(reverse=True)
# numeros.reverse()

# suma= sum(numeros)


# print(numeros)
# print(suma)


### TUPLAS ###

# datos=("nombre", 30, "True")
# nombre, edad, activo = datos
# print(datos)
# print(activo)
# print(nombre)
# print(edad)

# # print(dir(datos))
# elemento = (1,)
# print(len(elemento))
# print(elemento)


### CONJUNTOS (Sets)###

# basket = {"apple", "orange", "apple", "pear"}

# print(basket)

# frutas = {"manzana", "naranja", "platano"}

# frutas.add("pera")
# frutas.remove("naranja")
# print(frutas)


# citricos = {"naranja", "limon"}


# print(frutas & citricos)

### Diccionarios ###

# tel={
#     "jack":4098,
#     "sape": 4139
# }


### LAMBDA (funcion anonima) ###
# multiplicacion =lambda x, y: x*y

# print(multiplicacion(3,5))

