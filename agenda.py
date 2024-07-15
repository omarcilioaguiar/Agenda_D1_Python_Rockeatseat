# Desafio de agenda para salvar, editar, deletar e marcar um contato como favorito. 
# O resultado da aplicação deve ser apresentado no terminal, assim como foi visto no 
# módulo “Introdução ao Python” na Rockeatset.

def adicionar_contatos(contatos, nome_contato, telefone_contato, email_contato):
    # contato: nome do contato
    # favoritar: indicar se esse contato já foi favoritado ou não
    contato = {"contato": nome_contato, "telefone": telefone_contato, "email": email_contato, "favoritar": False}
    contatos.append(contato)
    print(f"O contato {nome_contato} foi adicionado com sucesso!")
    return

def ver_contatos(contatos):
    print("\nLista de Contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "❤" if contato["favoritar"] else " "
        nome_contato = contato["contato"]
        print(f"{indice}. [{status}] {nome_contato}")
    return

contatos = []
while True: 
    print("\nAgenda de Contatos - Desáfio:")
    print("1. Adicionar/Salvar Contato")
    print("2. Ver Contatos")
    print("3. Editar Contatos")
    print("4. Favoritar Contato")
    print("5. Deletar Contato")
    print("6. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_contato = input("Digite o nome do contato que deseja adicionar: ")
        telefone_contato = input("Digite o telefone deste contato")
        email_contato = input("Digite o email deste contato: ")
        adicionar_contatos(contatos, nome_contato, telefone_contato, email_contato)

    if escolha == "2":
        ver_contatos(contatos)
    
    if escolha == "6":
        print("Programa finalizado!")
        break