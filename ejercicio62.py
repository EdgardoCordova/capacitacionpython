# usando SORT las listas, ordenamiento del contenido

# array de strings
marcaCoches=["mazda","ford","vw","chevrolet"]
print(marcaCoches)

marcaCoches.sort()
print(marcaCoches)

# array de numeros
numeros=[1,9,88,65,46,13,22,8,7]
print(numeros)
numeros.sort()
print(numeros)
"""
# array combinado
combinado=[1,9,88,65,7,"mazda","ford","vw"]
print(combinado) 
#combinado.sort() # da un error pues eo ORDER no permite la combinación
print(combinado) # al menos que se conviertan los numeros a string
"""
"""
resultado:
['mazda', 'ford', 'vw', 'chevrolet']
['chevrolet', 'ford', 'mazda', 'vw']        
[1, 9, 88, 65, 46, 13, 22, 8, 7]
[1, 7, 8, 9, 13, 22, 46, 65, 88]
"""