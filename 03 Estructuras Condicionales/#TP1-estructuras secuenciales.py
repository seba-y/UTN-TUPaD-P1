#Estructuras condicionales - TP3

#Funciones para mejorar la estetica de los mensajes
def separar():
    input("\nPresiona enter para pasar a la siguiente actividad")
    print("-"*25)


################ ACTIVIDAD 1

edad = int(input("Ingrese su edad -> "))

if edad > 18:
    print("Es mayor de edad")

separar()

############# ACTIVIDAD 2

nota = int(input("Ingrese su nota -> "))

if nota >= 6:
    print("- Aprobado")
else:
    print("- Desaprobado")

separar()

############### Actividad 3

num = int(input("Ingrese un numero par -> "))

if num % 2 == 0:
    print("_Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par -> ")
    num = int(input())

separar()

############### Actividad 4

edad = int(input("ingrese su edad -> "))

if edad < 12:
    print("_Usted es un niño")
elif edad > 12 and edad < 18:
    print("_Usted es un adolescente")
elif edad >= 18 and edad < 30:
    print("_Usted es un adulto joven")
elif edad >= 30:
    print("_Usted es un adulto")

separar()

############### Actividad 5

contraseña = input("ingrese una contraseña que tenga más de 8 carácteres pero menos de 14. ->")

if 8 <= len(contraseña) <= 14:
    print("Se ha ingresado una contraseña correcta")
else:
    print("Por favor, ingresa una contraseña de entre 8 y 14 caracteres. ->")
    contraseña = input()

separar()

############### Actividad 6

import random
from statistics import mode, median, mean

random_numbers = [random.randint(1, 100) for i in range(50)]
media = mean(random_numbers)
mediana = median(random_numbers)
moda = mode(random_numbers)

print(f"La media es {media}\n")
print(f"la mediana es {mediana}\n")
print(f"la mode es {moda}")

separar()

############### Actividad 7

frase = input("Ingrese una frase o palabra -> ")

if frase[-1].lower() in "aeiou":
    frase += "!"
    
print(f"Resultado -> {frase}")

separar()

############### Actividad 8

name = input("Ingrese su nombre -> ")

print("Seleccione una opción:")
print("1 Mostrar el nombre en MAYÚSCULAS")
print("2 Mostrar el nombre en minúsculas")
print("3 Mostrar el nombre con la Primera Letra en mayúscula")

options = input("Ingrese 1, 2 o 3 -> ")

if options == "1":
    print("Resultado: ", name.upper())
elif options == "2":
    print("Resultado: ", name.lower())
elif options == "3":
    print("Resultado: ", name.title())
else:
    print("Opción no válida. Por favor, ingrese 1, 2 o 3.")

separar()

############### Actividad 9

magnitude = float(input("Ingrese la magnitud del terremoto en la escala de Richter -> "))
print("|\n|")
if magnitude < 3:
    print("Muy leve (imperceptible).")
elif 3 <= magnitude < 4:
    print("Leve (ligeramente perceptible).")
elif 4 <= magnitude < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitude < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitude < 7:
    print("Muy fuerte (puede causar daños significativos).")
else: 
    print("Extremo (puede causar graves daños a gran escala).")

separar()

################# actividad 10

def get_season(hemisphere, month, day):
    month = month.lower()
    seasons = {
        "norte": {
            "primavera": (("marzo", 21), ("junio", 20)),
            "verano": (("junio", 21), ("septiembre", 22)),
            "otoño": (("septiembre", 23), ("diciembre", 20)),
            "invierno": (("diciembre", 21), ("marzo", 20)),
        },
        "sur": {
            "primavera": (("septiembre", 23), ("diciembre", 20)),
            "verano": (("diciembre", 21), ("marzo", 20)),
            "otoño": (("marzo", 21), ("junio", 20)),
            "invierno": (("junio", 21), ("septiembre", 22)),
        }
    }

    seasons_ordered = list(seasons[hemisphere].items())
    
    for seasons, ((month_start, day_start), (month_end, day_end)) in seasons_ordered:
        if month == month_start and day >= day_start:
            return seasons.capitalize()
        elif month == month_end and day <= day_end:
            return seasons.capitalize()
        elif meses_entre(month, month_start, month_end):
            return seasons.capitalize()
    return "Fecha fuera de rango o inválida."


def meses_entre(month, start, end):
    months = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    s = months.index(start)
    e = months.index(end)
    m = months.index(month)
    if s < e:
        return s < m < e
    else:
        return m > s or m < e

hemisphere = input("¿En qué hemisferio estás? (norte o sur) -> ").lower()
month = input("¿Qué mes es? -> ").lower()
day = int(input("¿Qué día es? -> "))

if hemisphere not in ("norte", "sur"):
    print("Hemisferio no válido.")
else:
    season = get_season(hemisphere, month, day)
    print(f"Estás en {season}.")

input("Presione 'Enter' para finalizar el programa.")