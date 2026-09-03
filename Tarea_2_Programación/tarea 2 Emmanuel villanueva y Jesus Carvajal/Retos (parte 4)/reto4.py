n = input("Ingrese su nombre: ")
p = input("Ingrese el producto")
pp = float(input("Ingrese el precio del producto: "))
c = int(input("Ingrese la cantidad de productos: "))

st = pp * c
IVA = st * 0.19
tp = st + IVA

print("--------------------------------FACTURA--------------------------------")

print("Cliente: ",n)
print("Producto: ",p)
print("Cantidad: ",c)
print("Precio unitario: ",pp)

print("Subtotal: ",st)
print("IVA: ",IVA)
print("TOTAL: ",tp)

print("-----------------------------------------------------------------------")
