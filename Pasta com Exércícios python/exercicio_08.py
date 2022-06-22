'''8. Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A
formula de convers  ao  e:  C = K - 273.15, sendo C a temperatura em Celsius e K a
temperatura em Kelvin.'''

K = float(input("Entre com a temperatura em -Kelvin- que deseja converter para Celsius: "))
C = (K - 273.115)

print("O Resultado é:","%.2f" %C,"º")
