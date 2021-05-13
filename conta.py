import datetime
class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print("data abertura: {}".format(self.data_abertura))
        print("transações: ")
        for t in self.transacoes:
            print("-", t)

class Conta:
    def __init__(self, numero, cliente, saldo, limite=500.0):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()


    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("depósito de {}".format(valor))

    def saca(self, valor):
        if (self.saldo + self.limite) >= valor:
           self.saldo -= valor
           self.historico.transacoes.append("saque de {}".format(valor))
           return True
        else:
           return False

    def extrato(self):
        print("NUMERO: {} \nSALDO: {}\n".format(self.numero, self.saldo))
        self.historico.transacoes.append("tirou extrato - saldo de {}".format(self.saldo))

    def transfere(self, destino, valor):
        verificador = self.saca(valor)
        if verificador == True:
           destino.deposita(valor)
           self.historico.transacoes.append("transferencia de {} para conta {}".format(valor, destino.numero))
           return verificador
        else:
            return False

class Cliente:

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

