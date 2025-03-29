"""
Vetores e Matrizes
"""

#matriz = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
#]

#print("Elemento (0,0):", matriz[0][0])  
#print("Elemento (2,1):", matriz[2][1])

#for linha in matriz:
#    for elemento in linha:
#        print(f"|", end=" ")
#        print(elemento, end=' | ')
#    print()

"""
Exercicio 1
"""

#def ler_matriz_v1():
#    matriz = [[int(input(f"Digite o valor para [{i}][{j}]: ")) for j in range(4)] for i in range(4)]

#    for linha in matriz:
#        print(linha)

#def ler_matriz_v2():

#    matriz = []
#    for i in range(4):
#        linha = []
#        for j in range(4):
#            valor = int(input(f"Digite o valor para [{i}] [{j}]:"))
#            linha.append(valor)
#        matriz.append(linha)

#    for linha in matriz:
#        print(linha)

matriz = [

    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160],
]

#for linha in matriz_4_4:
#    for elemento in linha:
#        print (f"|", end=" ")
#        print (elemento, end=" | ")
#    print()

#soma = 0
#for i in range(4):
#        soma =soma + sum(matriz_4_4[i] ) 
#        print(f"A soma dos elementos acima e de: {soma}")


#soma = 0
#for linha in matriz_4_4:
#        soma =soma + sum (linha ) 
#        print(f"A soma dos elementos acima e de: {soma}")

#def Maior_Valor():
#    for linha in matriz_4_4:
#        maior = max(linha)
#        print(f"Maior valor da linha : {maior}")

"""
Contagem de Numeros Pares
"""
#def impar_par():
#    vet_pares = []
#    vet_impares = []
    
#    impares = 0
#    pares = 0

#    for i in range(4):
#        for j in range(4):
#            if matriz[i][j] % 2 == 0:
#                pares = pares + 1
#                vet_pares.append (matriz [i] [j])
#            else:
#                impares = impares + 1
#                vet_impares.append (matriz [i] [j])
#    print(f"Quantidade de numeros pares: {pares}")
#    print(f"Quantidade de numeros impares: {impares}")

#    print(f"os numeros pares sao: {vet_pares}")
#    print(f"os numeros impares sao: {vet_impares}")

"""
Multiplicação de Linhas por um Número
"""

def impar_par():

    num = int(input("Digite o número para multiplicação: "))
    linha_escolhida = int(input("Digite a linha a ser multiplicada (0-3): "))

    matriz[linha_escolhida] 
    for posiçao in range(4):
        matriz[linha_escolhida] = [num * valor for valor in matriz[linha_escolhida]]
        print(linha_escolhida)

#if __name__ == "__main__":
    #ler_matriz_v1()
    #ler_matriz_v2()
    #Maior_Valor()
    #impar_par()