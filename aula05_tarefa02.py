idade = int (input("qual e sua idade?"))
habilitado = input("voce tem carteira? <s/n>")
habilitado=habilitado.lower()

if (idade >= 18) and (habilitado == "s"):
 print("Você pode dirigir!")
else:
 print("Desculpe, sem carteira não dá!")