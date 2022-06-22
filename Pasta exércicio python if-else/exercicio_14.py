#14. A nota final de um estudante e calculada a partir de tres notas atribuıdas entre o intervalo
#de 0 ate 10, respectivamente, a um trabalho de laboratorio, a uma avaliacao semestral ˜
#e a um exame final. A media das tres notas mencionadas anteriormente obedece aos ˆ
#pesos: Trabalho de Laboratorio: 2; Avaliacao Semestral: 3; Exame Final: 5. De acordo ˜
#com o resultado, mostre na tela se o aluno esta reprovado (media entre 0 e 2,9), de 
#recuperac¸ao (entre 3 e 4,9) ou se foi aprovado. Faca todas as verificacoes necessarias


print("************************************************************")
print("************CALCULANDO NOTA FINAL DO ESTUDANTE**************")
print("************************************************************")

nota_trabalho_laboratorio = float(input("Entre com a nota do Trabalho do laboratório: "))
nota_avalicao_semestral = float(input("Entre com a nota da avaliação semestral: "))
exame_final = float(input("Entre com a nota do exame final: "))

media_ponderada = (nota_trabalho_laboratorio*2 + nota_avalicao_semestral*3 + exame_final*5)/10

if media_ponderada == 0 or media_ponderada <= 2.9:
    print(f"Você está reprovado sua média foi {media_ponderada:.2f}")

elif media_ponderada >= 3 and media_ponderada <= 4.9:
    print(f"Você está de recuperação sua média foi {media_ponderada:.2f}")

else:
      print(f"Você está aprovado sua média foi {media_ponderada:.2f}")

