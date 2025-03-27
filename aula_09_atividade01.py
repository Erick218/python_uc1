"""
Atividade 1
"""
vet_dados = [3, 10, 20, 30, 40, 50, 99, 88, 55, 76]

#def lista():
#    vetor = [10, 20, 30, 40, 50]
#    print("Vetor:", vetor)

#def lista_v2(vetor):
#    print("Vetor:", vetor)


"""
Atividade 2
"""

#def iterando_imprimindo(vetor):
#    for elemento in dados:
#        print("Elementos:", elemento)

"""
Atividade 3
"""

#import numpy as dados
#vector_np = dados.array([1, 2, 3, 4, 5])
#print("Vetor com Nupy:", vector_np)

""""
Atividade 4
"""

#def calcular_soma(vetor):
#    soma = sum(dados)
#    print("Soma dos elementos:", soma)


""""
Atividade 5
"""

#def Maior_Menor(vetor):
#    maior = max(vet_dados)
#    menor = min(vet_dados)
#    print("Maior valor", maior)
#    print("Menor valor", menor)


"""
Atividade 6
"""

#def inverter_ordem (vetor):
#    vetor_invertido = vet_dados[::-1]
#    print("Vetor invertido:", vetor_invertido)


"""
Atividade 7
"""

#def Multiplicar_elementos(vetor):
#    multiplicador = 2
#    vetor_mult = [elemento * multiplicador for elemento in vet_dados]
#    print("Vetor multiplicado:", vetor_mult)

"""
Atividade 8
"""

#def Contar_vetor(vetor):
#    ocorrencias = vet_dados.count(3)
#    print("O valor 3 aparece:", ocorrencias, "vesez.")

"""
Atividade 9
"""

#def vetor_crescente(vetor):
#    vetor_ordenado = sorted(vet_dados)
#    print("vetor ordenado:", vetor_ordenado)

"""
Atividade 10
"""
#def impar_par(vetor):
#    pares = [num for num in vet_dados if num % 2 == 0]
#    impares = [num for num in vet_dados if num % 2 != 0]
#    print("Impares", impares)
#print ("Pares", pares)

"""
Atividade 11
"""

def calcular_media(vetor):
    media = sum(vet_dados) / len(vet_dados)
    acima_media = [num for num in vet_dados if num > media]
    print("Media:", media)
    print("Elementos acima da media:", acima_media)

if __name__ == "__main__":
    #lista()
    #lista_v2(vet_dados)
    #inverter_ordem(vet_dados)
    #Maior_Menor(vet_dados)
    #calcular_soma(vet_dados)
    #iterando_imprimindo(vet_dados)
    #Multiplicar_elementos(vet_dados)
    #Contar_vetor(vet_dados)
    #vetor_crescente(vet_dados)
    #impar_par(vet_dados)
    calcular_media(vet_dados)