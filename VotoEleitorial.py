#Solicita ao usuário que informe a idade do eleitor 
idade =  int(input("Informe a idade do eleitor: "))
#verifica se é menor que 16 caso seja , aparecerá na tela que o voto é proibido
if idade < 16:
    print ("Voto Proibido")
#verifica se é menor de 18 caso seja , aparecerá na tela que o voto é optativo
elif idade < 18:
    print ("Voto Optativo")
#verifica se é menor de 65 caso seja , aparecerá na tela que o voto é obrigatorio
elif idade < 65:
    print ("Voto Obrigatório")
#caso não seja nenhum dos fatores anteriores aparecerá que o voto é optativo
else:
    print ("Voto Optativo")