nombre = input("ingrese su nombre: ")
peso = float(input("Ingrese su peso en kg: "))
Estatura = float(input("Ingrese su estatura en metros: "))

imc = peso/(Estatura)**2

print("=============DATOS===========")

print("nombre: ", nombre)
print("peso en kg: ", peso)
print("Estatura en metros: ", Estatura)
print("indice de masa corporal: ", round(imc, 2))