#Solicita a primeira,segunda e terceira nota do usuário e armazena em sua variáveis
nota1 = float(input("Qual a primeira nota  do aluno? "))
nota2 = float(input("Qual a segunda nota do aluno? "))
nota3 = float(input("Qual a terceira nota do aluno? "))

#Calcúla a média das 3 notas
media = (nota1 + nota2 + nota3) / 3

#agente de condição verifica se a média é maior ou igual a 7 e se for aparecerá "Aprovado"
if media >= 7.0:
    print("Aprovado")
#caso contrario o aluno que tirar menor que 7, aparecerá "Reprovado"
else:
    print("Reprovado")