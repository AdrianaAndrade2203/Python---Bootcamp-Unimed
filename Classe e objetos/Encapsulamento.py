#Em python utilizamos algumas convenções no nome do recurso para definir o acesso aos atributos e metodos
#da classe. Se for privado usamos um _ para definir.
#Publico pode ser acessado fora da classe
#Privado só pode ser acessado pela classe

class Conta:

    def __init__(self, saldo =0):
        self._saldo = saldo

    def depositar(self, valor):
        pass

    def sacar(self, valor):
        pass

# Apesar do python permitir, por conversão da declaração da variavel saldo ser privada pela declaração do _
#no nome, não devemos fazar da forma abaixo 

conta = Conta(100)
print(conta._saldo)
print(conta._saldo)


