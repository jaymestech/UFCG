# Algoritmo: Ler um número inteiro positivo e imprimir seus divisores.
# Ler um número inteiro positivo
num = int(input("Informe um número inteiro positivo: "))

# Imprimir os divisores do número
for i in range(1, num + 1):
    if num % i == 0:
        print(str(i) + " é divisor de " + str(num))