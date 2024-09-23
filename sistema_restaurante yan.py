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

print(""" 
        Cardápio
1 - Almôndega caseira R$: 20,00
2 - Arroz de forno R$: 25,00
3 - Bolo de carne vegano R$: 50,00
4 - Costelinha de porco R$: 75,00
5 - File de frango R$: 20,00
6 - Frango xadrez R$: 80,00
7 - Tutu de feijão R$: 90,00
""")



def opcoes():
    while True:
        opcao = input("Digite uma opção: ")
        match(opcao):
            case "1":
                preco = 20
                print("Almôndega caseira.")
            case "2":
                preco = 25
                print("Arroz de forno.")
            case "3":
                preco = 50
                print("Bolo de carne vegano.")
            case "4":
                preco = 75
                print("Costelinha de porco.")
            case "5":
                preco = 20
                print("File de frango.")
            case "6":
                preco = 80
                print("Frango xadrez.")
            case "7":
                preco = 90
                print("Tutu de feijão.")
            case _:
                print("Pedido invalido, digite novamente.")
                opcao = input("Digite um opção: ")
        return preco

opcao = opcoes()
    



