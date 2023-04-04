'''
Faça um programa que receba a data de hoje e a data de nascimento de uma pessoa e
mostre sua idade,as datas serãp recebidas em
um único inteiro no formato "DDMMAAAA"
'''
dataH = int(input("Informe a data de hoje num único inteiro no formato DDMMAAAA: "))
diaH = dataH // 1000000
mesH = dataH % 100000 // 10000
anoH = dataH % 10000

dataN = int(input("Informe a data de nascimento da pessoa num único inteiro no formato DDMMAAAA: "))
diaN = dataN // 1000000
mesN = dataN % 100000 // 10000
anoN = dataN % 10000
numAnos = anoH - anoN
if mesN < mesH:
    idade = numAnos - 1
elif mesN > mesH:
    idade = numAnos
else:
    if diaN < diaH:
        idade = numAnos
    else:
        idade = numAnos
print(f"A idade dessa pessoa é:", idade)