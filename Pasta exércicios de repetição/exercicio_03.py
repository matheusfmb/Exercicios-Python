'''3. Fac ̧a um algoritmo utilizando o comando while que mostra uma contagem regressiva
na tela, iniciando em 10 e terminando em 0. Mostrar uma mensagem “FIM!” ap  ́os a
contagem'''

import time
cont = 10

while cont >= 0:
    print (cont, end = " ")
    cont -=1
    time.sleep(0.5)
print ("\nThe Bomb has been exploded")