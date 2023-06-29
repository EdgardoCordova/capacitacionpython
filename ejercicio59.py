# eliminar un elemento de un array con REMOVE

# indice  0       1        2       3       4     5
frutasDulces=["uva","manzana","pera","banana","fresa"]
print(frutasDulces)

frutasDulces.remove("uva") # por nombre
print(frutasDulces)

frutasDulces.pop(2) # por indice
print(frutasDulces)

"""
resultado:
['uva', 'manzana', 'pera', 'banana', 'fresa']
['manzana', 'pera', 'banana', 'fresa']
['manzana', 'pera', 'fresa']
"""

