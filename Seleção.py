# Verificação de números que podem ser divididos em dois números de três algarismos cuja soma deles ao quadrado é igual ao número de 6 dígitos.

for num in range(100000, 1000000):
    str_num = str(num)
    if int(str_num[:3]) ** 2 + int(str_num[3:]) ** 2 == num:
        print(num)
