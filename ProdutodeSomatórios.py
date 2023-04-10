# Algoritmo para calcular o produto das somas
# (sum i = 1 to m x ^ i)(sum j = 1 to n y ^ j) =(x^ 1 +x^ 2 +***+x^ m )(y^ 1 +y^ 2 +***+y^ n )

# Ler os valores de m, n, x e y
m = int(input("Informe um valor inteiro positivo para m: "))
n = int(input("Informe um valor inteiro positivo para n: "))
x = float(input("Informe um valor real para x: "))
y = float(input("Informe um valor real para y: "))

# Calcular a soma de x elevado à potência de cada número de 1 até m
soma_x = 0
for i in range(1, m+1):
    soma_x += x**i

# Calcular a soma de y elevado à potência de cada número de 1 até n
soma_y = 0
for j in range(1, n+1):
    soma_y += y**j

# Calcular o produto das somas obtidas nos passos 2 e 3
produto = soma_x * soma_y

# Imprimir o resultado com 4 casas decimais
print("Produto das somas = {:.4f}".format(produto))