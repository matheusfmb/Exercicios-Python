from binascii import a2b_base64
from email.message import EmailMessage
import random
from tkinter import N

#a = (random.choice(range(1,100)))
#b = (random.choice(range(1,100)))

questao1 = int(input("Questão 1: Quanto é 20 + 20: "))
print("-------------------------------------------------")
questao2 = int(input("Questão 2: Qunato é 30 + 20: "))
print("----------------CORREÇÃO--------------------")

if questao1 == 40:
    acerto1 = 1
    print("Questão 1: 40 - você acertou")
else:
    acerto1 = 0
    print("Questão 1: 40 - você errou")

print("-------------------------------------")

if questao2 == 50:
    acerto2 = 1
    print("Questão 2: 50 - você acertou")
else:
    acerto2 = 0
    print("Questão 2: 50 - você errou")

print("-------------------------------------")

acertos = (acerto1+acerto2)
print(f"Você acertou {acertos}")

