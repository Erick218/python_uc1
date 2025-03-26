"""""
funçao imprimi uma mensagem de boas-vindas
"""

def saudacao():
    print("Olá, seja bem-vindo(a) ao curso de Python!")
    
# Chamando a função
saudacao()

if __name__ == "__main__":
    saudacao()

""""
funçao soma dois numeros e retorna o resultado
"""
def teste_soma():
    def soma(a, b):
        return a + b
    # Exemplo de chamada
    resultado = soma(5, 7)
    print(f"A soma é:, {resultado}")

if __name__ == "__main__":
    teste_soma()

""""
calcular o fatorial
"""
def teste_fatorial():
    def fatorial(n):
        if n < 0:
            return "Número inválido para fatorial."
        elif n == 0:
            return 1
        else:
            resultado = 1
            for i in range(1, n + 1):
                resultado *= i
            return resultado
# Exemplo de chamada
    numero=int(input("informe um numero:"))
    resultado=fatorial(numero)
    print (f"Fatorial de {numero} é igual à  {resultado}")

if __name__  =="__main__":
    teste_fatorial()
