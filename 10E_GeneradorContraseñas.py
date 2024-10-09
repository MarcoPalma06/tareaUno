#Marco Antonio Palma Rivera
#20192000607
from random import choice, randint, shuffle

def generarContraseña(longitud: int = 8):
  patron = ['M', 'm', 'n', 's']
  contraseña = ""

  patron += [choice(patron) for _ in range(longitud - 4)]
  shuffle(patron)

  for letra in patron:
    match letra:
      case 'M':
        contraseña += chr(randint(65, 90))
      case 'm':
        contraseña += chr(randint(97, 122))
      case 'n':
        contraseña += chr(randint(48, 57))
      case 's':
        contraseña += chr(choice([randint(33, 47), randint(58, 64), randint(91, 96)]))

  print(f"Contraseña generada es: {contraseña}")

while True:
    try:
        longitud = int(input("Ingrese la longitud de la contraseña: "))
        if longitud >= 8:
            break
        else:
            print("La longitud debe ser al menos de 8 caracteres.")
    except ValueError:
        print("Por favor, ingrese un numero valido.")

generarContraseña(longitud)