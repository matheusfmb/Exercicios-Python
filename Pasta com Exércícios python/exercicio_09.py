'''9. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A
formula de convers ´ ao ˜ e: ´ K = C + 273:15, sendo C a temperatura em Celsius e K a
temperatura em Kelvin.'''

C = float(input("Entre com a temperatua em Celsius que deseja converter para Kelvin: "))
K = (C + 273.15)

print("O resultado é:", "%.2f" %K,"º")