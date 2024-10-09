#Marco Antonio Palma Rivera
#20192000607

class CuentaBancaria:
    def __init__(self, titular: str, saldo: float = 0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad: float):
        self.saldo += cantidad

    def retirar(self, cantidad: float):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print('Fondos insuficientes')

    def mostrarSaldo(self):
        print(f'Titular: {self.titular}')
        print(f'Saldo: ${self.saldo}')

cuenta = CuentaBancaria('Marco Palma')
cuenta.mostrarSaldo()
cuenta.depositar(550)
cuenta.mostrarSaldo()
cuenta.retirar(275)
cuenta.mostrarSaldo()
cuenta.retirar(600)
cuenta.mostrarSaldo()