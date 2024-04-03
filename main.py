def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solicitar_numero(mensaje):
    while True:
        num = int(input(mensaje))
        if num > 0:
            return num
        else:
            print("El número debe ser positivo y diferente de cero.")

# Solicitar al usuario que ingrese los dos números
num1 = solicitar_numero("Ingresa el primer número (debe ser positivo y diferente de cero): ")
num2 = solicitar_numero("Ingresa el segundo número (debe ser positivo y diferente de cero): ")

# Calcular y mostrar el MCD
mcd = calcular_mcd(num1, num2)
print("El MCD de", num1, "y", num2, "es:", mcd)
