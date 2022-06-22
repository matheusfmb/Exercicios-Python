'''51. Tres amigos jogaram na loteria. Caso eles ganhem, o pr ˆ emio deve ser repartido pro- ˆ
porcionalmente ao valor que cada deu para a realizac¸ao da aposta. Fac¸a um programa ˜
que leia quanto cada apostador investiu, o valor do premio, e imprima quanto cada um ˆ
ganharia do premio com base no valor investido.'''


premio = float(input("Entre com o valor do prêmio: "))
jogador1 = float(input("Entre com o valor da aposta do jogador 1: "))
jogador2 = float(input("Entre com o valor da aposta do jogador 2: "))
jogador3 = float(input("Entre com o valor da aposta do jogador 3: "))
aposta_total = jogador1 + jogador2 + jogador3

p1 = jogador1*100/aposta_total
p2 = jogador2*100/aposta_total
p3 = jogador3*100/aposta_total

recebe1 = premio * p1/100
recebe2 = premio * p2/100
recebe3 = premio * p3/100


print(f"jogador 1 ganhará: {p1:.2f}% que é:{recebe1:.2f}")
print(f"jogador 2 ganhará: {p2:.2f}% que é:{recebe2:.2f}")
print(f"jogador 3 ganhará: {p3:.2f}% que é:{recebe3:.2f}")