'''5. Fac ̧a um programa que pec ̧ a ao usu  ́ario para digitar 10 valores e some-os.'''

n = 1
soma = 0
while n <= 10:
    x = int (input (f"Digite o {n} número"))
    soma = soma + x
    n = n + 1
print (f"Soma: {soma}")