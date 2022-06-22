'''21. Leia um valor de massa em libras e apresente-o convertido em quilogramas. A f  ́ormula
de convers  ̃ao  ́e: K = L∗0,45, sendo K a massa em quilogramas e L a massa em libras.'''

libras = float(input("Entre com o valor em libras: "))
quilos = libras*0.45

print(f"O resultado em quilogramas é {quilos:.2f}")
