#10. Fac¸a um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu
#peso ideal, utilizando as seguintes formulas (onde ´ h corresponde a altura): `
#• Homens: (72:7 ∗ h) − 58
#• Mulheres: (62; 1 ∗ h) − 44; 7

h = float(input("Entre com sua altura: "))
sexo = int(input("Digite 1 para homem, 2 para mulher: "))

if sexo == 1:
   peso_ideal = (72.7*h)-58
   print(f"Seu peso ideal é: {peso_ideal:.2f}")
else:
    peso_ideal = (62.1*h)-44.7
    print(f"Seu peso ideal é: {peso_ideal:.2f}")
    



