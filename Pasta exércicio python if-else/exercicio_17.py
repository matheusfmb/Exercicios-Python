#17. Fac ̧ a um programa que calcule e mostre a  ́area de um trap  ́ezio. Sabe-se que:
#A = (basemaior + basemenor) ∗altura
#2
#Lembre-se a base maior e a base menor devem ser n  ́umeros maiores que zero
print("************************************************************")
print("*************CALCULADORA DE ÁREA DO TRAPÉZIO****************")
print("************************************************************")

base_maior = float(input("Entre com a base maior: "))
base_menor = float(input("Entre com a base menor: "))
altura = float(input("Entre com a  altura: "))

if base_maior < 0 or base_menor < 0:
    print("As bases devem ser positivas.")
else:
    area = (base_maior + base_menor)*altura/2
    print(f"A base do trapézio é: {area:.2f}")
    