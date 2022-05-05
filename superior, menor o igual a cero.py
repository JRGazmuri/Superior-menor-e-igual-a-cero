igual_cero = 0
menor_cero = 0
mayor_cero = 0
num = 0
cant = 1
y = int(input("Total numeros enteros\n"))
for char in range(y):
    x = int(input(f"valor {cant}:\n"))
    cant = cant + 1
    if x == 0:
        igual_cero = igual_cero + 1
        print ("el valor es cero")
    elif x < 0:
        menor_cero = menor_cero + 1
        print ("el valor es menor que cero")
    else:
        mayor_cero = mayor_cero + 1
        print ("el valor es mayor que cero")
print(f"Los números iguales a cero son {igual_cero}.\nLos números menores a cero son {menor_cero}.\nLos múmeros mayores a cero son {mayor_cero}.\nDe un total de {y} numeros enteros.")