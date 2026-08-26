a, b = 10, 25

print("Antes del intercambio 'a': ", a)
print("Antes del intercambio 'a': ", b)

def intercambio(a, b):
    
    a, b = b, a
    
    print("a: ", a)
    print("b: ", b)
    
    
intercambio(a, b)