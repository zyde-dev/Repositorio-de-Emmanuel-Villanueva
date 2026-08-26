codigo = int(input("Ingrese codigo del estudiante: "))
nombre = input("Ingrese nombre del estudiante: ")
edad = int(input("Ingrese edad del estudiante: "))
programa = input("Ingrese programa del estudiante: ")
semestre = int(input("Ingrese semestre del estudiante: "))
materias = int(input("Numero de materias matriculadas: "))
valor_materia = float(input("Ingrese valor de cada materia: "))

valor_total = materias * valor_materia

print("================================================")
print(            "REGISTRO DE MATRICULAS"              )
print("================================================")

print("Codigo del estudiante: ", codigo)
print("Nombre del estudiante: ", nombre)    
print("Edad del estudiante: ", edad)
print("Programa del estudiante: ", programa)
print("Semestre del estudiante: ", semestre)
print("Numero de materias matriculadas: ", materias)
print("Valor de cada materia: ", valor_materia)
print("Valor total a pagar: ", valor_total)

print("================================================")

