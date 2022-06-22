#22. Leia a idade e o tempo de servic ̧o de um trabalhador e escreva se ele pode ou n  ̃ao se
#aposentar. As condic ̧  ̃oes para aposentadoria s  ̃ao
#• Ter pelo menos 65 anos,
#• Ou ter trabalhado pelo menos 30 anos,
#• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.


idade = int(input("Entre com sua idade: "))
tempo_servico = float(input("Entre com o tempo de serviço em anos: "))

if idade >= 65: 
    print("Você pode se aponsentar.")

elif tempo_servico > 30:
    print("Você pode se aposentar.")

elif idade >= 60 and tempo_servico >= 25:
    print("Você pode se aposentar")

else:
    print("Você não pode se aposentar")
