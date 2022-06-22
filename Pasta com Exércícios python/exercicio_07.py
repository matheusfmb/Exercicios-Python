#Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
#A formula de convers ´ ao ˜ e: ´ C = 5:0 ∗ (F − 32:0)=9:0, sendo C a temperatura em Celsius
#e F a temperatura em Fahrenheit.

temperatura_f = float(input("Entre com a temperatura em º Fahrenheit: "))
temperatura_c = 5*(temperatura_f - 32)/9

print("%.1f" %temperatura_f,'º Fahrenheit é',"%.1f"%temperatura_c,"º Celsius")