# manejo de strings .... usando 'format' en string, usando indices 
# ayuda a combinar string con variables de una manera más ordenada

cantidad=3
numeroID=123456
precio=59.90

# siempre comenzar con el valor 0 en el arrray 
precioDeVenta="El producto vale {1} y son {2} productos, el número de contro es {0}"

# el orden cambio en relación al ejercicio30.py
print(precioDeVenta.format(numeroID,precio,cantidad)) 
