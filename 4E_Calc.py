#Marco Antonio Palma Rivera
#20192000607

class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sumar(self):
        return self.a + self.b

    def restar(self):
        return self.a - self.b

    def multiplicar(self):
        return self.a * self.b

    def dividir(self):
        if self.b == 0:
            return "Indefinido"
        return self.a / self.b

print("Calculadora")

a = None
b = None

while True:
    try:
        if a == None:
            a = int(input("Digite el primer número: "))
        b = int(input("Digite el segundo número: "))
        break
    except ValueError:
        print("Numero invalido")

calculadora = Calculadora(a, b)

print(f"  {a} + {b} = {calculadora.sumar()}")
print(f"  {a} - {b} = {calculadora.restar()}")
print(f"  {a} * {b} = {calculadora.multiplicar()}")
print(f"  {a} / {b} = {calculadora.dividir()}")