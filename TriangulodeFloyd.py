# Algoritmo: O Triângulo de Floyd é uma construção que consiste em escrever uma sequência de números naturais consecutivos, iniciando com 1, na primeira linha, seguido de 2 3 na segunda, e assim por diante.

# leitura do valor de n
n = int(input("Informe um inteiro positivo para n: "))

# variável para controle do número a ser impresso
num = 1

# loop para imprimir o Triângulo de Floyd
for i in range(1, n+1):
    # loop para imprimir cada linha do Triângulo de Floyd
    for j in range(1, i+1):
        # imprime o número e um espaço em branco
        print(num, end=" ")
        # incrementa o valor do número a ser impresso
        num += 1
    # quebra de linha para imprimir a próxima linha
    print()
