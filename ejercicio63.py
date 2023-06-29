# usando SORT las listas, ordenamiento invertido del contenido 
# con reverse....... numeros.sort(reverse=True)

# array de strings
marcaCoches=["mazda","ford","vw","chevrolet"]
print(marcaCoches)

marcaCoches.sort(reverse=True)
print(marcaCoches)

# array de numeros
numeros=[1,9,88,65,46,13,22,8,7]
print(numeros)
numeros.sort(reverse=True)
print(numeros)

"""
resultado:
['mazda', 'ford', 'vw', 'chevrolet']
['vw', 'mazda', 'ford', 'chevrolet']
[1, 9, 88, 65, 46, 13, 22, 8, 7]
[88, 65, 46, 22, 13, 9, 8, 7, 1]
"""
