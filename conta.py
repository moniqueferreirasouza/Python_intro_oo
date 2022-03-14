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

    def __pode_retirar(self, valor_a_retirar):
        valor_disponivel_retirada = self.__saldo + self.__limite
        return valor_a_retirar <= (valor_disponivel_retirada)

    def retira(self, valor):
        if(self.__pode_retirar(valor)):
            self.__saldo -= valor
        else:
            print("O saque {} é maior que o valor permitido, seu saque máximo é de {}.".format(valor, self.__saldo + self.__limite))

    def transfere(self, valor, destino):
        self.retira(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property#permite executar getters and setters e acessar atributos privados declarando de forma simples. Ex: conta.limite
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod#Cria um método visível para chamar um resultado não modificável
    def codigo_banco():
        return "001"

    @staticmethod#Cria um método visível para chamar um resultado não modificável
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

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