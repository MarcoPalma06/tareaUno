#Marco Antonio Palma Rivera
#20192000607

while True:
    try:
        n = int(input("Digite un número: "))
        break
    except ValueError:
        print("Digito no valido") 

if n < 2:
    esPrimo = False
else:
    esPrimo = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            esPrimo = False
            break
        
if esPrimo:
    print(f"{n} es un número primo")
else:
    print(f"{n} no es un número primo")