#def apresentar(nome, idade):
# print(f"Nome: {nome}, Idade: {idade}")
#apresentar("Alice", 30) # Posicional
#apresentar(idade=30, nome="Alice") # Nomeado

#def saudacao(nome="Mundo"):
# print(f"Olá, {nome}!")
#saudacao("erick") # Saída: Olá, Mundo!
#saudacao("Alice") # Saída: Olá, Alice!
#saudacao()

#def listar_nomes(*nomes):
# for nome in nomes:
#    print(nome)
#listar_nomes("Alice", "2", "Charlie")

#def listar_frutas(*frutas):
#    for fruta in frutas:
#        print(fruta)
#listar_frutas("Maça", "Banana", "melancia")

#def saudacao():
#    print("Olá do módulo!")
#if __name__ == "__main__":
#    saudacao()

import sys

def soma(args):
    for arg in args:
        print(arg)

def soma (numeros) :
    somatorio = 0
    for valor in numeros :
        somatorio = somatorio + float(valor)

    #print(f"O valor da soma dos números é {somatorio}")
    return somatorio

if __name__ == "__main__":
    resultado=soma(sys.argv[1:])
    print(f"o valor da soma dos números é {resultado}")