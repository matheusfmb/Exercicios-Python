s = 0
for c in range(1,7):
    num = int(input("Entre com o valor {}: ".format(c)))
    if num % 2 == 0:
        s+=num
print(f"Soma dos valores pares é = {s}")