#Mesmo codigo do arquivo 01, porem com acesso aos metodos e variaveis de forma correta pelas convenções

class Conta:

    def __init__(self, nro_agencia, saldo =0):
        self.nro_agencia = nro_agencia
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo 


conta = Conta("0001", 100)
conta.depositar(500)
conta.sacar(50)
print(conta.nro_agencia)
print(conta.mostrar_saldo())
