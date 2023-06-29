# de 2 arrays crear uno solo

# indice  0       1        2       3       4     5
frutasDulces=["uva","manzana","pera","banana","fresa"]
frutasNodulces=["aguacate","tomate"]
print(frutasDulces)
print(frutasNodulces)

cestoFrutas=[]
cestoFrutas.extend(frutasDulces)
cestoFrutas.extend(frutasNodulces)

print(cestoFrutas)


"""
resultado:
['uva', 'manzana', 'pera', 'banana', 'fresa']
['aguacate', 'tomate']
['uva', 'manzana', 'pera', 'banana', 'fresa', 'aguacate', 'tomate']
"""

