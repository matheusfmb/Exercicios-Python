#23. Faca um algoritmo que leia um numero positivo e imprima seus divisores

num = int(input("Entre com o número: "))
print("Seus divisores são")
i = 1
divisores = 0

while i <= num:
    if num%i == 0:
        divisores += 1
    i+=1

print(divisores)
