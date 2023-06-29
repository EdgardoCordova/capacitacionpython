# arrays (listas) e indices reemplazar un valor

# indice  0       1        2       3
frutas=["uva","manzana","pera","banana","fresa"]
print(frutas)

# reemplazamos un rango
print(frutas[1:3])      # primer numero es el indice inicial, y el segundo valor es la ultima columna
frutas[1:3]=["jocote","sandia"] 
print(frutas)

#  reemplazar de varios valores, en un array
j=(len(frutas))
i=0
while i<j:
    frutas[i]="-"
    i+=1
print(frutas)

""""
resultado:
['uva', 'manzana', 'pera', 'banana', 'fresa']
['manzana', 'pera']
['uva', 'jocote', 'sandia', 'banana', 'fresa']
['-', '-', '-', '-', '-']
"""