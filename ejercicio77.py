# uniendo los diccionarios, atencion cuando {} y cuando()
# se pueden poner varios valores

frutasVerdes={"manzana","pera"}
frutasMaduras={"sandia","jocote"}

# unir diccionarios 
frutasMaduras.update(frutasVerdes)
print(frutasMaduras)

"""
resultado:
{'jocote', 'manzana', 'sandia', 'pera'}
"""
