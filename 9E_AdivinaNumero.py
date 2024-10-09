#Marco Antonio Palma Rivera
#20192000607
from random import randint

numero = randint(1, 100)
intentos = 0

while True:
    intento = int(input("Adivina el numero: "))
    intentos += 1
    if intento == numero:
        print(f"Adivinaste el numero en {intentos} intentos")
        break
    elif intento < numero:
        print("Intenta con un numero mayor entre el 1 y el 100")
    else:
        print("Intenta con un numero menor entre el 1 y el 100")