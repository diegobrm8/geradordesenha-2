class AgendaContatos:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone, email):
        self.contatos[nome] = {'telefone': telefone, 'email': email}
        print(f"Contato {nome} adicionado com sucesso!")

    def buscar_contato(self, nome):
        if nome in self.contatos:
            contato = self.contatos[nome]
            print(f"Nome: {nome}\nTelefone: {contato['telefone']}\nEmail: {contato['email']}")
        else:
            print(f"Contato {nome} não encontrado na agenda.")

    def listar_contatos(self):
        print("Lista de Contatos:")
        for nome, contato in self.contatos.items():
            print(f"Nome: {nome}\nTelefone: {contato['telefone']}\nEmail: {contato['email']}\n")

def main():
    agenda = AgendaContatos()

    while True:
        print("\nOpções:")
        print("1. Adicionar Contato")
        print("2. Buscar Contato")
        print("3. Listar Contatos")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            email = input("Digite o email do contato: ")
            agenda.adicionar_contato(nome, telefone, email)

        elif escolha == '2':
            nome = input("Digite o nome do contato que deseja buscar: ")
            agenda.buscar_contato(nome)

        elif escolha == '3':
            agenda.listar_contatos()

        elif escolha == '4':
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
