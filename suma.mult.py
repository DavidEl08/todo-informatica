

def sum(a, b):
    """funcio qeu suma """
    resultado = a + b
    return (resultado)
def mul(a, b):
    """funcio qeu multiplicacion """
    resultado = a * b
    return (resultado)

a = int(input('a? '))
b = int(input('b? '))

print(f'Sum de {a} y {b} : {sum(a, b)}')
print(f'mul de {a} y {b} : {mul(a, b)}')
