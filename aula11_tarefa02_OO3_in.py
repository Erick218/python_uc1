class Conta:
    def __init__(self, numero, nome, limite):
        self.numero = numero
        self.nome = nome
        self.limite = limite
        self.saldo = 0
        
    
    def depositar (self, valor):
        print(f"Saldo inicial: {self.saldo}")
        self.saldo = self.saldo + valor
        print(f"Saldo final : {self.saldo}")


    def sacar (self, saque):
       print(f"Saldo inicial: {self.saldo}")
       #self.saldo = self.saldo - valor

       if valor > self.limite:
           self.saldo = self.saldo - valor

       print(f"Saldo final : {self.saldo}")

    def info(self):
        print(f"conta: {self.numero} -- {self.nome} -- {self.saldo}")



class Banco:
    def __init__(self):
        self.Conta = {}

if __name__ == "__main__":
    cc_1= Conta ("0001", "Papagaio", 1500.20)
    cc_1.info()
    valor_deposito=float(input("Digite o valor do deposito :"))
    cc_1.deposito{valor_deposito}
    #cc_1.depositar(100)"""
