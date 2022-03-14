

#Cria o endereço do objeto
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        #O self.xxx faz uma busca pelo valor declarado que está armazenado

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def retira(self, valor):
        self.saldo -= valor






