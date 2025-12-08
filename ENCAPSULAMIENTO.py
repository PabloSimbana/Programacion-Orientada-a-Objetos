class CuentaBancaria:
    def __init__(self, saldo):
        self._saldo = saldo  # atributo protegido

    def obtener_saldo(self):
        return self._saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad

    def retirar(self, cantidad):
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
