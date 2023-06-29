# diccionarios o SETS son como arrays con {  }

frutas={"zapote","sandia"}
print(frutas)
frutas.add("jocote")    # podemos agregar mas elemnto con ADD, no APPEND.
print("Escriba una fruta a agregar: ")
nuevaFruta=input()
frutas.add(nuevaFruta)   # 
print(frutas)

"""
resultado(favor revisen el orden en que se da todo, pues no hay un orden como en el APPEND)
{'zapote', 'sandia'}
Escriba una fruta a agregar: 
granadilla
{'zapote', 'granadilla', 'jocote', 'sandia'}
"""