""""
Calculadora Simples
"""

import sys

def teste_calculadora_simples():

    def operaçoes (args):
        for arg in args:
            print (args)
    def numeros (n1 , n2 ,op ):
        
        for n2 in (n1 , n2 ,op):
        
            if op == "+":
                resultado=n1+n2
        
            elif op == "-":
                resultado=n1-n2
        
            elif op == "*":
                resultado=n1*n2
        
            elif op == "/":
                resultado=n1/n2

            if __name__ == "__main__":
                argumentos=sys.argv[1:]
                numero1=float(argumentos(0))
                numero2=float(argumentos(1))
                operaçao=argumentos[2]
                teste_calculadora_simples (f"(numero1) (operaçao) (numero2)")
            
                    