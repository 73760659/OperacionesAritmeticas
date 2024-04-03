def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Solicitar al usuario que ingrese el primer número, validando que no sea negativo ni cero
while True:
    num1 = int(input("Ingresa el primer número (debe ser positivo y diferente de cero): "))
    if num1 > 0:
        break
    else:
        print("El número debe ser positivo y diferente de cero.")

# Solicitar al usuario que ingrese el segundo número, validando que no sea negativo ni cero
while True:
    num2 = int(input("Ingresa el segundo número (debe ser positivo y diferente de cero): "))
    if num2 > 0:
        break
    else:
        print("El número debe ser positivo y diferente de cero.")

# Calcular y mostrar el MCD
mcd = calcular_mcd(num1, num2)
print("El MCD de", num1, "y", num2, "es:", mcd)
