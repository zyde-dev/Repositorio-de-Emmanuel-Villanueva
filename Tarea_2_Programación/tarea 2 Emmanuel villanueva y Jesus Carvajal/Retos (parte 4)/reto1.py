nombre = input("Ingrese su nombre:")
precio = float(input("Ingrese el precio del producto:"))
prebebi = float(input("Ingrese el precio de la bebida:"))
personas = int(input("Ingrese el numero de personas:"))

total = (precio + prebebi) * personas
vxperosna = total / personas

print("El total a pagar es:", total)
print("El total a pagar por persona es:", vxperosna)