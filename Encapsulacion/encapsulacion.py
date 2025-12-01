class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, monto):
        self.__saldo += monto

    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
        else:
            print("Fondos insuficientes")

    def obtener_saldo(self):
        return self.__saldo


cuenta = CuentaBancaria("Juan", 100)
cuenta.depositar(50)
cuenta.retirar(30)

print("Saldo final:", cuenta.obtener_saldo())
