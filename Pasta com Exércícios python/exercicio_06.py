'''Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A formula de convers ´ ao ˜ e: ´ F = C∗(9:0/5:0)+32:0, sendo F a temperatura em Fahrenheit
e C a temperatura em Celsius.'''

temperatura_c = float(input("Entre com a temperatura em º Celsius: "))
temperatura_f = temperatura_c*(9/5)+32

print(temperatura_c,"º", "é", temperatura_f,"º", "em gaus Fahrenheit ")
