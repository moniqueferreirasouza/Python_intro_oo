

def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def retira(conta, valor):
    conta["saldo"] -= valor

def extrato(conta, saldo):
    print("Seu saldo atual é {}".format(conta[saldo]))