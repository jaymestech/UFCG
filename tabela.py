#1.Ler um número inteiro positivo N
#2.Imprimir a frase "Início da tabela:"
#3.Criar a repetição de i = N até i = 0,tirando i a cada interação
#4.Imprimir o valor de i na primeira coluna e o dobro de i na segunda coluna
#5.Imprimir a frase "Fim da tabela!"


n = int(input("Informe um valor inteiro positivo para N: "))

print("Início da tabela:")
for i in range(n, -1, -1):
    print(f"{i} {2*i}")
print("Fim da tabela!")
