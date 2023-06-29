# diccionarios
# nombre:valor
# nombres son claves
# valores : oscar, develoteca.com, develoteca, 39

nombres={"nombre":"Oscar","sitio":"develoteca.com","canal":"develoteca","edad":39 }
print(nombres)

print(nombres["canal"])
print(nombres["sitio"])
print(nombres.get("edad"))

"""
resultado:
{'nombre': 'Oscar', 'sitio': 'develoteca.com', 'canal': 'develoteca', 'edad': 39}
develoteca    
develoteca.com
39
"""

