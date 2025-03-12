numero = float(input("digie um numero"))
if numero > 0:
    print("esse numero e positivo")
elif numero < 0:
    print("esse numero e negativo")
else:
    print("esse numero e 0")


idade =  int(input("diga sua idade"))
if idade >= 16:
    print("voce tem 16 ou mais anos,voce pode votar")
else:
    print("voce nao tem mais de 16 anos portanto nao pode votar")


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
if numero1 > numero2:
    print(f"O maior número é {numero1}.")
elif numero2 > numero1:
    print(f"O maior número é {numero2}.")
else:
    print("Os dois números são iguais.")


numero = int(input("digite um numero"))
if numero % 2== 0:
    print("O numero e par")
else:
    print("O numero e impar")


usuario = input("digite um usuario")
senha =  input("digite uma senha")
if usuario == "admin" and senha == "1234":
    print("Acesso permitido")
else:
    print("acesso negado")
