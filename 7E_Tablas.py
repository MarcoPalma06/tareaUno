#Marco Antonio Palma Rivera
#20192000607

while True:
    try:
        numero = int(input("Digite un número entero para ver su tabla de multiplicar: "))
        break
    except ValueError:
        print("El un número debe de ser un entero")
for i in range(1, 13):
    print(f"{numero} x {i} = {numero * i}")