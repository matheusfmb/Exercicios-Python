import random
import time


print("************************************************************")
print("*****************PEDRA-PAPEL-TESORUA************************")
print("************************************************************")
while True:
    print("-----------------------------")
    print(""" Faça sua jogada.
    1 - PAPEL
    2 - PEDRA
    3 - TESOURA""")
    print("-----------------------------")
    jogada_jogador = int(input("Entre com a sua jogada: "))
    print("-----------------------------")
    jogada_computador = (random.choice(range(1,3)))

    if jogada_jogador != 1 and jogada_jogador != 2 and jogada_jogador != 3:
        print("Jogada Inválida")

    elif jogada_jogador == 1:
        print("Jogador jogou Papel.")
        print("----------------------")
        if jogada_computador == 2:
            time.sleep(1)
            print("Computador jogou Pedra.")
            print("----------------------")
            time.sleep(1)
            print('\033[0;30;41mJogador Venceu\033[m')
            print("\U0001f600") 
            
        elif jogada_computador == 3:
            time.sleep(1)
            print("Computador jogou Tesoura.")
            print("----------------------")
            time.sleep(1)

            print('\033[0;30;41mJogador Perdeu\033[m')
            
        elif jogada_computador == 1:
            time.sleep(1)
            print("Computador jogou Papel.")
            print("----------------------")
            time.sleep(1)
            print('\033[0;30;41mEmpate\033[m')
            
    elif jogada_jogador == 2:
        print("Jogador jogou Pedra.")
        if jogada_computador == 1:  
            time.sleep(1)
            print("Computador jogou Papel.")
            print("----------------------")
            time.sleep(1)
            print('\033[0;30;41mJogador Perdeu\033[m')
            
        elif jogada_computador == 2:
            time.sleep(1)
            print("Computador jogou Pedra.")
            print("----------------------")
            time.sleep(1)
            print('\033[0;30;41mEmpate\033[m')
            
        elif jogada_computador == 3:
            print("Computador jogou Tesoura")
            time.sleep(1)
            print("----------------------")
            time.sleep(1)
            print('\033[0;30;41mJogador Venceu\033[m')
            print("\U0001f600")
            
    elif jogada_jogador == 3:
        print("jogador jogou Tesoura.")
        if jogada_computador == 1:
            time.sleep(1)
            print("Computador jogou Papel.")
            print("----------------------")
            print('\033[0;30;41mJogador Venceu\033[m')
            time.sleep(1)
            print("\U0001f600") 
          
        elif jogada_computador == 2:
            time.sleep(1)
            print("Computador jogou Pedra.")
            print("----------------------")
            time.sleep(1)
            print('\033[0;30;41mJogador Perdeu\033[m')
            
        elif jogada_computador == 3:
            time.sleep(1)
            print("Computador jogou Tesoura")
            print("----------------------")
            time.sleep(1)
            print('\033[0;30;41mEmpate\033[m')
            print("----------------------")
            
        
    sair = (input("Deseja sair? digite sair se não pressione qualquer tecla: "))
    if sair.upper().strip() == "SAIR":
        break
time.sleep(3)




        








    