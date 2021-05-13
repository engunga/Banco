from conta import Conta

c1 = Conta('548-7','Ezequiel', 500, 500)
c2 = Conta('125-8', 'Moli', 50, 1000)
c1.extrato()
c1.deposita(100)
c1.extrato()
c1.transfere(c2,1000)
c1.extrato()
c2.extrato()

c1.saca(101)
c1.historico.imprime()
c2.historico.imprime()