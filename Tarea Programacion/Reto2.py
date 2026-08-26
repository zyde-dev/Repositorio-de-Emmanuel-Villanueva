#FACTURA RESTAURANTE


Nombre_cliente = input("Ingrese nombre de cliente: ")
Valor_comida = int(input("Ingrese el valor de la comida: "))
valor_bebidas = int(input("Ingrese el valor de la bebida: "))

Subtotal = Valor_comida + valor_bebidas

propina = (Subtotal*10)/100

total_pagar = Subtotal+propina

print("------------------FACTURA--------------------")
print("Nombre cliente: ", Nombre_cliente)
print("Subtotal: ", Subtotal)
print("propina 10%: ", propina)
print("total a pagar: ", total_pagar)
