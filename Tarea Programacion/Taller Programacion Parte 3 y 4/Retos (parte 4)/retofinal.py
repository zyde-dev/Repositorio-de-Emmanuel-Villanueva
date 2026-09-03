nv = input("Ingrese el nombre del vendedor: ")
nc = input("Ingrese el nombre del cliente: ")
p = input("Ingrese el producto: ")
c = int(input("Ingrese la cantidad de productos: "))
pu = float(input("Ingrese el precio unitario del producto: "))

st = pu * c
desc = st * 0.10
IVA = st * 0.19
tp = (st - desc) + IVA

print("================== VENTA ===================")

print("Vendedor: ",nv)
print("Cliente: ",nc)
print("Producto: ",p)
print("Cantidad: ",c)

print("Subtotal: ",st)
print("Descuento: ",desc)
print("IVA: ",IVA)

print("TOTAL A PAGAR: ",tp)

print("============================================")