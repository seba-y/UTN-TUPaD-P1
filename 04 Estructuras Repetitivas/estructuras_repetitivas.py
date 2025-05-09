######
def separador():
    input("Presione Enter para continuar...")
    print("-"*50)

def inicio(num):
    print(f"_Ejercicio {num}:\n|\n|")

#Ejercicio 1
#_________________________________________________________
inicio(1)
for i in range(101):
    print(i)

separador()

#Ejercicio 2
#_________________________________________________________
inicio(2)
print("Ingrese un numero entero para saber la cantidad de digitos -> ")
num = int(input(""))
num_letras = len(str(num))
print(f"El numero tiene ( {num_letras} )digitos")

separador()

#Ejercicio 3
#_________________________________________________________
inicio(3)
print("Ingrese dos números enteros para sumar todos los valores comprendidos entre estos dos")
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
if num1 > num2:
    num1, num2 = num2, num1
elif num1 == num2:
    print("Los numeros son iguales, no se puede sumar ya que no tienen numeros de por medio")
res = sum(range(num1 + 1, num2))
print(f"La suma de los numeros comprendidos entre {num1} y {num2} es ( {res} ) ")

separador()

#Ejercicio 4
#_________________________________________________________
inicio(4)
print("_Ingrese numeros enteros para sumarlos en secuencia.\n_Ingrese 0 para detener la suma.")
num = int(input(""))
sum = 0
while num != 0:
    sum += num
    num = int(input(""))

print(f"Usted ha frenado el programa.\nLa suma de los numeros ingresados es ( {sum} )")

separador()

#Ejercicio 5
#_________________________________________________________
import random
adivinanza = random.randint(0, 9)
num_intentos = 1

inicio(5)
print("Adivine el número con la menor cantidad de intentos posibles...\n_PISTA: Es un número del 0 al 9")
num = int(input("Número -> "))
while num != adivinanza:
    print("NO!! intenta devuelta...")
    num = int(input("Número -> "))
    num_intentos += 1
    
print(f"ADIVINASTE!! el número era ( {adivinanza} )!!!\nLo lograste en ( {num_intentos} ) intentos")
separador()

#Actividad 6
#_________________________________________________________
inicio(6)
print("Los números pares que se encuentran entre el 0 y el 100 son...")
numeros_pares = []
for i in range(0, 101):
    if i % 2 == 0:
        numeros_pares.insert(0,i)
print(numeros_pares)

separador()

#Actividad 7
#_________________________________________________________
inicio(7)
print("Ingrese un numero entero para calcular la suma de todos los numeros comprendidos entre 0 y este")
num = int(input(""))
sum = 0
while num <= 0:
    print("El numero ingresado no es valido, ingrese un numero positivo")
    num = int(input(""))
for i in range(0, num + 1):
    sum += i
print(f"La suma de todos los numeros comprendidos entre 0 y {num} es ( {sum} )")

separador()

#Actividad 8
#_________________________________________________________
inicio(8)
print("ingrese 100 numeros enteros para saber cuantos son positivos, negativos y cuantos son pares e impares")
nums = []
nums_pares = []
nums_impares = []
nums_positivos = []
nums_negativos = []
for i in range(100):
    num = int(input(""))
    nums.append(num)
    if num % 2 == 0:
        nums_pares.append(num)
    else:
        nums_impares.append(num)
    if num > 0:
        nums_positivos.append(num)
    else:
        nums_negativos.append(num)

print("Usted ha ingresado 100 números")
print(f"De los cuales:\n_{len(nums_pares)} son pares\n_{len(nums_impares)} son impares\n_{len(nums_positivos)} son positivos\n_{len(nums_negativos)} son negativos")

separador()

#Actividad 9
#_________________________________________________________
inicio(9)
import statistics
nums = []
media_nums = 0

print("Ingrese 100 numeros enteros para calcular la media de los mismos")
for i in range(100):
    num = int(input(""))
    nums.append(num)
media_nums = statistics.mean(nums)

print(f"La media de los numeros ingresados es ( {media_nums} )")

separador()

#Actividad 10   
#_________________________________________________________
inicio(10)
print("_Ingrese un número y te devuelvo el número invertido...\n_Ejemplo: 1234 -> 4321")
num = input("")
while len(num) < 1:
    num = input("El numero ingresado no es valido, ingrese un numero con más de 1 dígito -> ")

num_invertido = num[::-1]
print(f"El numero invertido es ( {num_invertido} )")
print("_"*100)

input("Presione Enter para finalizar el programa...")


