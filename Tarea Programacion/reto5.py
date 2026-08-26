print("-------------CODIGO ERRADO-----------------")
try:
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    nueva_edad = edad + 5
    print(nombre)
    print(nueva_edad)
except TypeError:
    print("Error.")

#El codigo tiene un error ya que intenta sumar un entero con un texto
#input() esta devolviendo un texto y no un numero
#Deberia colocarse int() para convertir el tetxo en un entero

print("-------------CODIGO CORREGIDO-----------------")
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
nueva_edad = edad + 5
print(nombre)
print(nueva_edad)
