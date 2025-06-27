
def carregar_dados(arquivo):
    """Carrega os dados de pessoas do arquivo."""
    try:
        with open(arquivo, 'r') as f:
            dados = {}
            for linha in f:
                nome, idade = linha.strip().split(',')
                dados[nome] = int(idade)
            return dados
    except FileNotFoundError:
        return {}

def salvar_dados(arquivo, dados):
    """Salva os dados das pessoas no arquivo."""
    with open(arquivo, 'w') as f:
        for nome, idade in dados.items():
            f.write(f"{nome},{idade}\n")

def menu():
    print("--- MENU DE CADASTRO ---\n")
    print("1. Cadastrar pessoa")
    print("2. Alterar idade")
    print('3. Remover pessoa')
    print("4. Listar pessoas")
    print('5. Sair e salvar')

def main():
    arquivo = 'pessoas.txt'
    pessoas = carregar_dados(arquivo)

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            if nome in pessoas:
                print("Essa pessoa já está cadastrada.")
            else:
                try:
                    idade = int(input("Idade: "))
                    pessoas[nome] = idade
                    print("Pessoa cadastrada com sucesso!")
                except ValueError:
                    print("Idade inválida.")

        elif opcao == '2':
            nome = input("Digite o nome da pessoa para alterar a idade: ")
            if nome in pessoas:
                try:
                    nova_idade = int(input("Nova idade: "))
                    pessoas[nome] = nova_idade
                    print("Idade atualizada.")
                except ValueError:
                    print("Idade inválida.")
            else:
                print("Pessoa não encontrada.")

        elif opcao == '3':
            nome = input('Digite o nome da pessoa a ser removida: ')
            if nome in pessoas:
                del pessoas[nome]
                print('Pessoa removida .')
            else:
                print("Pessoa não encontrada.")

        elif opcao == '4':
            if pessoas:
                print("\nLista de pessoas cadastradas:")
                for nome, idade in pessoas.items():
                    print(f"Nome: {nome}, Idade: {idade}")
            else:
                print("Nenhuma pessoa cadastrada.")

        elif opcao == '5':
            salvar_dados(arquivo, pessoas)
            print("Dados salvos. Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
