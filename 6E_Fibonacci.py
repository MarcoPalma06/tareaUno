#Marco Antonio Palma Rivera
#20192000607

while True:
    try:
        num = int(input("Digita el límite de la serie de Fibonacci: "))
        if num < 0:
            print("El número debe ser positivo")
        else:
            break
    except ValueError:
        print("Ingrese un número entero")

def fibonacci(num2):
    if num2 == 0:
        return 0
    elif num2 == 1:
        return 1
    else:
        return fibonacci(num2-1) + fibonacci(num2-2)

for i in range(num):
    if i < num-1:
        print(fibonacci(i), end=", ")
    else:
        print(fibonacci(i), end="\n")