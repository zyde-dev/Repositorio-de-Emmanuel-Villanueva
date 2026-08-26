nombre_producto = input("Ingrese nombre del producto: ")
precio = int(input("Ingrese el precio del producto:"))
cantidad = int(input("Ingrese la cantidad de porductos:"))

subtotal = precio * cantidad

print("Producto: ",nombre_producto)
print("Precio unitario: $",precio)
print("Cantidad: ",cantidad)
print("Total: $",subtotal)
