# manejo de strings .... usando 'format' en string. 
# ayuda a combinar string con variables de una manera más ordenada

cantidad=3
numeroID=123456
precio=59.90

precioDeVenta="El producto vale {} y son {} productos, el control número de contro es {}"

print(precioDeVenta.format(precio,cantidad,numeroID))
