# TUPLAS como modificar (pero no es la idea)

marcasCarros=("mazda","ford","toyota")
print(marcasCarros)
marcasCarrosTemporal=list(marcasCarros) # usar LIST

marcasCarrosTemporal.append("audi")  # OJO con sintaxis
marcasCarros=tuple(marcasCarrosTemporal) # usar TUPLE
print(marcasCarros)

"""
resultado
('mazda', 'ford', 'toyota')
('mazda', 'ford', 'toyota', 'audi')
"""