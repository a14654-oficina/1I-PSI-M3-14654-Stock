
print("\nOs materiais que tens em stock são: ", file=ficheiro)
print("1. Papel")
print("2. Borracha")
print("3. Lápis")
print("4. Afias")
print("5. Canetas")

def adicionar_material(stock):
    nome = input("Nome do material: ")
    if nome in stock:
        print("O material já existe no stock!")
    else:
        quantidade = int(input(f"Quantidade inicial de {nome}: "))
        stock[nome] = quantidade
        print(f"{nome} adicionado com sucesso!")

def consultar_stock(stock):
    nome = input("Nome do material para consulta: ")
    if nome in stock:
        print(f"O stock atual de {nome} é: {stock[nome]}")
    else:
        print(f"{nome} não encontrado no stock.")

def atualizar_stock(stock):
    nome = input("Nome do material a atualizar: ")
    if nome in stock:
        operacao = input("Deseja adicionar (A) ou remover (R)? ").upper()
        quantidade = int(input("Quantidade: "))
        if operacao == "A":
            stock[nome] += quantidade
            print(f"{quantidade} unidade(s) adicionada(s) ao stock de {nome}.")
        elif operacao == "R":
            if quantidade <= stock[nome]:
                stock[nome] -= quantidade
                print(f"{quantidade} unidade(s) removida(s) do stock de {nome}.")
            else:
                print("Quantidade insuficiente em stock!")
        else:
            print("Operação inválida!")
    else:
        print(f"{nome} não encontrado no stock.")

def exibir_stock(stock):
    print("\nEstado Geral do Stock:")
    print("Material\tQuantidade")
    print("-" * 30)
    for material, quantidade in stock.items():
        print(f"{material}\t\t{quantidade}")

def main():
    stock = {}
    while True:
        print("\nGestão de Stock")                     
        print("1. Adicionar Material")
        print("2. Consultar Stock")
        print("3. Atualizar Stock")
        print("4. Exibir Stock Geral")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_material(stock)
        elif opcao == "2":
            consultar_stock(stock)
        elif opcao == "3":
            atualizar_stock(stock)
        elif opcao == "4":
            exibir_stock(stock)
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()

A opção 1 adiciona um material ao stock.
A opção 2 consulta e diz quantos materiais estão no stock atual.
A opção 3 atualiza o stock do material dito anteriormente.
A opção 4 diz-nos tudo o que tem no stock atual tanto de lápis, canetas etc…
A opção 5 sai do programa no mesmo instante.


O \t server para dar um tablado

Adicionar_material pergunta o nome e a quantidade do material que quer adicionar.
consultar_stock consulta o material que colocou no adicionar_material
atualizar_Stock atualiza todos os materiais que estão no stock
exibir_stock exibe todos os materiais e a quantidade que tem no stock  
   

