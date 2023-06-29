# ejemplo ejercicio con WHILE
# aplicacion que le pida al usuario una cantidad 
# determinada de numeros, mostar numeros impares

i=1
print("Ingrese cuanto ciclos desea ...")
ciclos=int(input())

while i<=ciclos:
    if (i%2)==1:
        print(i,"impar")
    i+=1
else:
    print("se acabo")

