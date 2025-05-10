#funciones para separar las actividades
def separador():
    input("\nPresione Enter para continuar al menú...")
    print("_" * 50)
    menu()

def inicio():
    print("-"*50)
    

def menu():
    print("Menú de navegación \n")

    for i in range(1, 11):
        print(f"Ingrese el número {i} para ir a la actividad ( {i} )")
    inicio()
    i = int(input("Ingrese el número de la actividad -> "))
    seleccionar_actividad(i)



def seleccionar_actividad(i):

    if i == 1:
        actividad1()
    elif i == 2:
        actividad2()
    elif i == 3:
        actividad3()
    elif i == 4:
        actividad4()
    elif i == 5:
        actividad5()
    elif i == 6:
        actividad6()    
    elif i == 7:
        actividad7()
    elif i == 8:
        actividad8()
    elif i == 9:
        actividad9()
    elif i == 10:
        actividad10()


###### ACTIVIDAD 1 ######

def actividad1():
    inicio()    
    numeros_multiplos_4 = []
    print("___Actividad 1___")
    for i in range(1, 101):
        if i % 4 == 0:
            numeros_multiplos_4.append(i)
    print(f"Los números múltiplos de 4 son: {numeros_multiplos_4}")
    separador()

###### ACTIVIDAD 2 ######

def actividad2():
    inicio()
    print("___Actividad 2___")
    list = ["Pastas","Futbol","hongos","gatos",22]
    print(f"El penúltimo elemento de la lista es: {list[-2]}")
    separador()

###### ACTIVIDAD 3 ######

def actividad3():
    inicio()
    print("___Actividad 3___")
    list = []
    list.append("Pastas")
    list.append("Futbol")
    list.append("hongos")
    print("Estos son los elementos de la lista:")
    print(list)
    separador()

###### ACTIVIDAD 4 ######

def actividad4():
    inicio()
    print("___Actividad 4___")
    animales = ["perro", "gato", "conejo", "pez"]
    animales[1] = "loro"
    animales[-1] = "oso"
    print(animales)
    separador()

###### ACTIVIDAD 5 ######

def actividad5():
    inicio()
    print("___Actividad 5___")
    print("Explicación del siguiente programa:")
    inicio()
    print("numeros = [8,15,3,22,7]\nnumeros.remove(max(numeros))\nprint()numeros")
    inicio()    
    print("Lo que hace este programa es:\n_Primero se crea una lista con 5 numeros enteros\n_Despues se remueve el número más alto\n_Y por último se imprime toda la lista, ahora con 4 elementos.")
    separador()

###### ACTIVIDAD 6 ######

def actividad6():
    inicio()
    print("___Actividad 6___")
    lista = list(range(10,30,5))
    print(lista[:2])
    separador()

###### ACTIVIDAD 7 ######

def actividad7():
    inicio()
    print("___Actividad 7___")
    autos = ["sedan", "polo", "suran", "gol"]
    print(f"lista sin cambios {autos}")

    autos[1:3] = ["BMW", "Aston martin"]
    print(f"lista con los cambios {autos}")
    separador()

###### ACTIVIDAD 8 ######

def actividad8():
    inicio()
    print("___Actividad 8___")
    dobles = []
    dobles.append(5*2)
    dobles.append(10*2)
    dobles.append(15*2)
    print(dobles)
    separador()

###### ACTIVIDAD 9 ######

def actividad9():
    inicio()
    print("___Actividad 9___")
    compras = [["pan","leche"], ["arroz", "fideos", "salsa"], ["agua"]]

    compras[2].append("jugo")
    compras[1][1] ="tallarines"
    compras[0].remove("pan")

    print(compras)
    separador()

###### ACTIVIDAD 10 ######

def actividad10():
    inicio()
    print("___Actividad 10___")
    lista_anidada = [15,True,[25.5,57.9,30.6],False]
    print(lista_anidada)
    separador()

menu()