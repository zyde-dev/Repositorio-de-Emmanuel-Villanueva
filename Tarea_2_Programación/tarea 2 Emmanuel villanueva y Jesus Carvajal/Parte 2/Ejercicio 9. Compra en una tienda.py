#Solicitar:
#Nombre del producto
#Precio
#Cantidad
#Calcular el valor total.
#Ejemplo:
#Producto: Cuaderno
#Precio: 8500
#Cantidad: 3
#Total a pagar: $25500

nombre_producto = input("Ingrese el nombre del producto: ")
precio_producto = float(input("Ingrese el precio del producto: "))
cantidad_producto = float(input("Ingrese la cantidad que va a comprar: "))
total_pagar = precio_producto*cantidad_producto
print("//")
print("Producto: ", nombre_producto)
print("Precio: ", precio_producto)
print("Cantidad: ", cantidad_producto)
print("Total a pagar: $",total_pagar)