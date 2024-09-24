"""
Informe o número da turma: 
Turma - 93313

Nome completo dos componentes.
1 - Maria Luiza Campos
2 - Yan Mendes Matos
"""



import os

# Limpa o terminal.
os.system("cls || clear") 

def cardapio():
    print(""" 
                 Cardápio    
codigo   |        pratos           |   preços  
    1      Almôndega caseira        R$: 20,00
    2      Arroz de forno           R$: 25,00
    3      Bolo de carne vegano     R$: 50,00  
    4      Costelinha de porco      R$: 75,00
    5      File de frango           R$: 20,00
    6      Frango xadrez            R$: 80,00
    7      Tutu de feijão           R$: 90,00
""")

def opcoes(carrinho, pratos_selecionados):
    while True:
        cardapio()
        opcao = input("Digite uma opção: ")
        
        match opcao:
            case "1":
                carrinho.append(20)
                pratos_selecionados.append("Almôndega caseira")
            case "2":
                carrinho.append(25)
                pratos_selecionados.append("Arroz de forno")
            case "3":
                carrinho.append(50)
                pratos_selecionados.append("Bolo de carne vegano")
            case "4":
                carrinho.append(75)
                pratos_selecionados.append("Costelinha de porco")
            case "5":
                carrinho.append(20)
                pratos_selecionados.append("File de frango")
            case "6":
                carrinho.append(80)
                pratos_selecionados.append("Frango xadrez")
            case "7":
                carrinho.append(90)
                pratos_selecionados.append("Tutu de feijão")
            case _:
                print("Pedido inválido, digite novamente.")
                opcao = input("Digite uma opção: ")

        print(f"Você pediu: {pratos_selecionados[-1]} - Preço: R$ {carrinho[-1]:.2f}")

        opcao2 = input("""\nDeseja pedir novamente:
            1 - Sim
            2 - Não
            0 - Encerrar
            R: """)
        
        if opcao2 == "2":
            return sum(carrinho)
        elif opcao2 == "0":
            return sum(carrinho)

carrinho = []
pratos_selecionados = []
preco_total = opcoes(carrinho, pratos_selecionados)

def forma_de_pagamento(preco_total):
    forma_pagamento = input("""\n             Forma de pagamento
1 - À Vista (10% de Desconto)
2 - Cartão de Crédito (10% de Acréscimo)
R: """)
    
    match forma_pagamento:
        case "1":
            desconto = preco_total * 0.10
            valor = preco_total * 0.90
            forma = "À Vista"
            acréscimo = 0
        case "2":
            acréscimo = preco_total * 0.10
            valor = preco_total * 1.10
            forma = "Cartão de Crédito"
            desconto = 0
        case _:
            print("Opção inválida. O total será considerado sem alteração.")
            valor = preco_total
            forma = "Nenhuma"
            desconto = 0
            acréscimo = 0
    
    return valor, forma, desconto, acréscimo

valor_total, forma_pagamento, desconto, acréscimo = forma_de_pagamento(preco_total)

# Exibindo os resultados
print("\nResultados:")
print("Pratos escolhidos:")
for i, prato in enumerate(pratos_selecionados):
    print(f"{i+1} - {prato}")


print(f"\nSubtotal: R$ {preco_total:.2f}")
print(f"Forma de pagamento: {forma_pagamento}")
if forma_pagamento == "À Vista":
    print(f"Desconto aplicado: R$ {desconto:.2f}")
else:
    print(f"Acréscimo aplicado: R$ {acréscimo:.2f}")
print(f"Valor final a ser pago: R$ {valor_total:.2f}")
