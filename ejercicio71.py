# TUPLAS  una mejor asignacion de valores a tuplas

marcasCarros=("mazda","ford","toyota","vw","chevrolet")
print(marcasCarros)

# desempaquetar (o asignacion) datos de TUPLAS
(marca1,marca2,*marca3)=marcasCarros  # marcaX como variables, observar *
# en *marca3  se almacenaran los datos posteriores..."toyota","vw","chevrolet"
print(marca1)
print(marca2)
print(marca3)
"""
resultado:
('mazda', 'ford', 'toyota', 'vw', 'chevrolet')
mazda
ford
['toyota', 'vw', 'chevrolet']
"""