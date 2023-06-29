# unir 3 arrays o listas, deja unir strings con numeros.....+ + +
# por lo que es una mejor opción que EXTENT

# indice  0       1        2       3       4     5
frutasDulces=["uva","manzana","pera","banana","fresa"]
frutasNodulces=["aguacate","tomate"]
otroListado=[1,6,3]

print(frutasDulces)
print(frutasNodulces)
print(otroListado)

cestoFrutas=[]
cestoFrutas=frutasDulces+frutasNodulces+otroListado
print(cestoFrutas)

"""
resultado:
['uva', 'manzana', 'pera', 'banana', 'fresa']
['aguacate', 'tomate']
['uva', 'manzana', 'pera', 'banana', 'fresa', 'aguacate', 'tomate']
"""
