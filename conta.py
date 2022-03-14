#Cria o endereço do objeto
class Conta:
    def __init__(self, numero, titular, saldo, limite = 1000.0):
        print("Construindo objeto ...{}".format(self))
        self.__numero = numero #__ serve para privar o atributo e não permitir sua edição fora do código (encapsular)
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        #O self.xxx faz uma busca pelo valor declarado que está armazenado

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def retira(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.retira(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


"""
Aqui são os comandos utilizados no console do PyCharm para realizar as consultas

from conta import Conta #informa o arquivo py e puxa a classe desejada
conta = Conta (123, "Monique", 300.0, 500.0) #cria um novo objeto dentro da classe
conta2 = Conta (321, "Joao", 100.0, 500.0) 
conta._Conta__saldo #consulta o saldo
conta.extrato() #extrato do saldo
conta2.retira(20) #saque
conta2.transfere(70.0, conta) #transferência

"""