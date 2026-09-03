#Solicitar:
#Nombre del empleado
#Número de horas trabajadas
#Valor de la hora
#Calcular el salario
#Ejemplo:
#Salario = horas trabajadas × valor hora
#Mostrar:
#Empleado: Pedro
#Salario: $1200000

nombre_empleado = input("Ingrese el nombre del empleado: ")
horas_trabajadas = float(input("Ingrese el numero de horas trabajadas: "))
valor_hora = float(input("Ingrese el valor de las horas trabajas: "))

salario = horas_trabajadas*valor_hora
print("//")
print("Empleado: ", nombre_empleado)
print("Salario: ", salario)