# crear una pequeña aplicacion IMC indice de masa corporal 
# IMC = peso / (altura)2

print("Proporciona el peso en KG")
peso =input()
print("Proporciona la altura en metros")
altura =input()
peso=float(peso)
altura=float(altura)

imc=peso/(altura*altura)
print("su IMC es de ",imc)
