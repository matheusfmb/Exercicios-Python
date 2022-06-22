
import random

rodadas = 5
pontuacao = 0
respostas_acertadas = 0

perguntas = ["De quem é a famosa frase “Penso, logo existo”? \n a) Platão \n b) Galileu Galilei \n c) Descartes \n d) Sócrates \n e) Francis Bacon", 
"De onde é a invenção do chuveiro elétrico? \n a) França \n b) Inglaterra \n c) Brasil \n d) Austrália \n e) Itália", 
"Quais o menor e o maior país do mundo? \n a) Vaticano e Rússia \n b) Nauru e China \n c) Mônaco e Canadá \n d) Malta e Estados Unidos \n e) São Marino e Índia",
"Qual o nome do presidente do Brasil que ficou conhecido como Jango? \n a) Jânio Quadros \n b) Jacinto Anjos \n c) Getúlio Vargas \n d) João Figueiredo \n e) João Goulart", 
"Quantas casas decimais tem o número pi \n a) Duas \n b) Centenas \n c) Infinitas \n d) Vinte \n e) Milhares",
"O que a palavra legend significa em português? \n a) Legenda \n b) Conto \n c) História \n d)Lenda \n e) Legendário",
"Qual o número mínimo de jogadores numa partida de futebol? \n a) 8 \n b) 10 \n c) 9 \n d) 5 \n e) 7",
"Em que período da pré-história o fogo foi descoberto? \n a) Neolítico \n b) Paleolítico \n c) Idade dos Metais \n d) Período da Pedra Polida \n e) Idade Média",
"Em qual local da Ásia o português é língua oficial? \n a) Índia \n b) Filipinas \n c) Moçambique \n d) Macau \n e) Portugal",
"Quem é o autor de “O Príncipe”? \n a) Maquiavel \n b) Antoine de Saint-Exupéry \n c) Montesquieu \n d) Thomas Hobbes \n e) Rousseau"]
respostas = ["C","C","A","E","C","D","E","B","D","A"]

print("O jogo tem 5 rodadas")
for i in range(5):
    pergunta = (random.choice(range(0,len(perguntas))))
    print(i+1,".",perguntas[pergunta])
    while True:
        resposta = input("Entre com a alternativa: ").upper()
        if resposta not in respostas:
            print("Alternativa inválida")
            continue
        else:
            break
    if resposta == respostas[pergunta]:
        print("você acertou")
        respostas_acertadas +=1
        pontuacao += 100
        perguntas.pop(pergunta)
        respostas.pop(pergunta)
    else:
        print("Você errou")
        pontuacao += 0
        print(f"sua pontuação foi: {pontuacao}")
        break
    print("--------------------------------------")

if respostas_acertadas == 5:
    print(f"Você Acertou todas as rodadas. sua pontuação foi: {pontuacao}")



    


