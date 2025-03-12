# Exibir cabeçalho da tabela
print("A | B | A AND B")
print("--| --|--------")

#Gerar todas as combinaçoes de A e B
for A in [0,1]:
    for B in [0,1]:
        resultado = A and B # Operaçoes AND
        print(f"{A} | {B} |  {resultado}")