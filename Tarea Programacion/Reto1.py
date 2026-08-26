#RETO #1

Nombre_del_empleado = input("Ingrese nombre: ")
Número_horas_trabajadas = int(input("Ingrese horas trabajadas: "))
Valor_de_cada_hora = int(input("Ingrese su salario por hora"))

salario = Número_horas_trabajadas * Valor_de_cada_hora

print("----------------COMPROBANTE---------------------------")
print("Empleado: ", Nombre_del_empleado)
print("Horas trabajadas: ", Número_horas_trabajadas)
print("Valor por hora: ", Valor_de_cada_hora)
print("salario: ", salario)