# lê dois números reais da entrada
num1 = float(input("Informe o primeiro operando: "))
num2 = float(input("Informe o segundo operando: "))

# lê o operador da entrada
operador = input("Informe o operador (+, -, * ou /): ")

# verifica qual operação deve ser realizada
if operador == "+":
    resultado = num1 + num2
    operacao = "adição"
elif operador == "-":
    resultado = num1 - num2
    operacao = "subtração"
elif operador == "*":
    resultado = num1 * num2
    operacao = "multiplicação"
elif operador == "/":
    if num2 == 0:
        print("Divisão por zero inválida!")
        exit()
    resultado = num1 / num2
    operacao = "divisão"
else:
    print("Operador inválido!")
    exit()

# exibe o resultado
print(f"Resultados da operação = {operacao} {resultado}")
