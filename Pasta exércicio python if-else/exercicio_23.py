#24. Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado
#possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS
#8%). Fac ̧a um programa em que o usu  ́ario entre com o valor e o estado destino do
#produto e o programa retorne o prec ̧ o final do produto acrescido do imposto do estado
#em que ele ser  ́a vendido. Se o estado digitado n  ̃ao for v  ́alido, mostrar uma mensagem
#de erro.

valor_produto = float(input("Entre com o valor do produto: "))
estado = str(input("""
Entre com a sigla do estado:
MG - Minas Gerais
SP - São paulo
RJ - Rio de Janeiro
MS - Mato grosso:  """)).upper()

if estado != "MG" and estado != "SP"  and estado != "RJ" and estado != "MS":
    print("Entre com uma sígla válida")
    exit()
elif estado == "MG" :
    imposto = valor_produto*0.07
    valor_final = imposto + valor_produto
    print(f"O valor do produto em MG é {valor_final}")
elif estado == "SP" :
    imposto = valor_produto*0.12
    valor_final = imposto + valor_produto
    print(f"O valor do produto em SP é {valor_final}")
elif estado == "RJ" :
    imposto = valor_produto*0.15
    valor_final = imposto + valor_produto
    print(f"O valor do produto em RJ é {valor_final}")
elif estado == "MS":
    imposto = valor_produto*0.08
    valor_final = imposto + valor_produto
    print(f"O valor do produto em MS é {valor_final}")
exit()