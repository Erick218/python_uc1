#Verificação de Acesso ao Sistema


idade = int (input("qual e a sua idade?"))
senha = input("qual a sua senha?")

if (idade >= 18) and (senha == "1234"):
    print ("acesso permitido")
else:
    print("acesso negado")


#Aprovado na Faculdade?
    

numero1 = float (input("Digite a primeira nota:"))
numero2 = float (input("Digite a segunda nota"))
media=(numero1 + numero2)/2

trab_extra=input("Entregou o  trabalho extra <s/n>")

if (media >=7) or (trab_extra=="s") :
    print("!!! Voce foi aprovado!!!")
else:
    print("voce nao foi aprovado")


 #Controle de Entrada em uma Festa


idade = int (input("qual e a sua idade?"))
acompanhado=input("voce esta acompanhado? <s/n>")

if (idade >= 18) or (acompanhado == "s"):
    print("Voce pode entrar!")
else:
    print("Voce nao pode entrar!")