#20. Dados tres valores, ˆ A, B, C, verificar se eles podem ser valores dos lados de um triangulo ˆ
#e, se forem, se e um triangulo escaleno, equilatero ou isoscele, considerando os seguin- ´
#tes conceitos:

#• O comprimento de cada lado de um triangulo ˆ e menor do que a soma dos outros ´
#dois lados.

#• Chama-se equilatero o tri ´ angulo que tem tr ˆ es lados iguais. ˆ
#• Denominam-se isosceles o tri ´ angulo que tem o comprimento de dois lados iguais. ˆ
#• Recebe o nome de escaleno o triangulo que tem os tr ˆ es lados diferentes.

A = int(input("Entre com o valor A: "))
B = int(input("Entre com o valor B: "))
C = int(input("Entre com o valor C: "))

if A > (B+C) or B > (A+C) or C > (A+B):
    print("Um lado do triângulo não poder ser maior que a soma dos outros dois lados.")

elif A == B and A == C:                         
    print("Esse Triângulo é equilatero, pois possui três lados iguais.")

elif A == B or C == B:
    print("Esse Triângulo é isosceles, pois tem dois lados iguais.")
    
else:
    print("Esse trinângulo é escaleno, pois possui três lados diferentes.")
 


