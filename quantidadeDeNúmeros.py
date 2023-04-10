# Algoritmo:
# 1. Ler a quantidade de números a serem contados
# 2. Inicializar contadores
# 3. Para cada número lido:
# 3.1. Verificar se é negativo, zero, positivo, par ou ímpar e incrementar o respectivo contador
# 4. Imprimir os contadores

# Passo 1
quantidade = int(input("Qual a quantidade de reais a serem contados? "))

# Passo 2
negativos = 0
zeros = 0
positivos = 0
pares = 0
impares = 0

# Passo 3
for i in range(quantidade):
    valor = float(input("Informe um valor real qualquer: "))
    if valor < 0:
        negativos += 1
    elif valor == 0:
        zeros += 1
    else:
        positivos += 1
    
    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1

# Passo 4
print(f"Quantidade de valores negativos = {negativos}")
print(f"Quantidade de valores zeros = {zeros}")
print(f"Quantidade de valores positivos = {positivos}")
print(f"Quantidade de valores pares = {pares}")
print(f"Quantidade de valores ímpares = {impares}")
