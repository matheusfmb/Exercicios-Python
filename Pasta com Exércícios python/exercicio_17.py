'''17. Leia um valor de comprimento em cent´ımetros e apresente-o convertido em polegadas.
A formula de convers ´ ao ˜ e: ´ P = C
2;54, sendo C o comprimento em cent´ımetros e P o
comprimento em polegadas.'''

C = float(input("Entre com o comprimento em centímetros: "))
P = (C/2.54)

print("o resultado em polegadas é: ", "%.3F" %P)
