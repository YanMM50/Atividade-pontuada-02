"""
Informe o número da turma: 
Turma - 93313

Nome completo dos componentes.
1 - Maria Luiza Campos
2 - Yan Mendes Matos
"""


import osg

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
        match (opcao):
            case "1":
                resultado = "Almôndega caseira."
                print("Almôndega caseira.")
            case "2":
                resultado = "Arroz de forno."
                print("Arroz de forno.")
            case "3":
                resultado = "Bolo de carne vegano."
                resultado = "Bolo de carne vegano."
            case "4":
                resultado = "Costelinha de porco."
                resultado = "Costelinha de porco."
            case "5":
                resultado = "File de frango."
            case "6":
                resultado = "Frango xadrez."
            case "7":
                resultado = "Tutu de feijão."
            case _:
                print("Pedido invalido, digite novamente.")
        return resultado

opcao = opcoes()
    


