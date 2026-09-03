#Solicitar el radio y calcular:
#Área = 3.1416 × radio²

radio_ciculo = float(input("Ingrese el radio del circulo en cm: "))
import math
area= math.pi*radio_ciculo
print(f"El area del circulo es: , {area:.2f}", "cm")