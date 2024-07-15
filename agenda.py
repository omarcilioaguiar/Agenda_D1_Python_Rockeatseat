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
        status = "❤ " if contato["favoritar"] else " "
        nome_contato = contato["contato"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]
        print(f"{indice}. [{status}] {nome_contato} - {telefone_contato} - {email_contato}")
    return

def editar_nome_contato(contatos, indice_contato, novo_nome_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["contato"] = novo_nome_contato
        print(f"Nome do Contato {indice_contato} atualizado para {novo_nome_contato}")
    else:
        print("Indice de contato inválido!")
    return

def editar_telefone_contato(contatos, indice_contato, novo_telefone_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["telefone"] = novo_telefone_contato
        print(f"Nome do Contato {indice_contato} atualizado para {novo_telefone_contato}")
    else:
        print("Indice de contato inválido!")
    return

def editar_email_contato(contatos, indice_contato, novo_email_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["email"] = novo_email_contato
        print(f"Nome do Contato {indice_contato} atualizado para {novo_email_contato}")
    else:
        print("Indice de contato inválido!")
    return

def favoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    contatos[indice_contato_ajustado]["favoritar"] = True
    print(F"Contato {indice_contato} favoritado com sucesso!")
    return

def desfavoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    contatos[indice_contato_ajustado]["favoritar"] = False
    print(F"Contato {indice_contato} desfavoritado com sucesso!")
    return

def ver_contato_favoritos(contatos):
    print("\nLista de Contatos Favoritos:")
    favoritos = [contato for contato in contatos if contato["favoritar"]]
    for indice, contato in enumerate(favoritos, start=1):
        status = "❤ "
        nome_contato = contato["contato"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]
        print(f"{indice}. [{status}] {nome_contato} - {telefone_contato} - {email_contato}")
    return

def deletar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if 0 <= indice_contato_ajustado < len(contatos):
        contato_removido = contatos.pop(indice_contato_ajustado)
        print(f"Contato {contato_removido['contato']} deletado com sucesso!")
    else:
        print("Índice de contato inválido!")
    return

contatos = []
while True: 
    print("\nAgenda de Contatos - Desáfio:")
    print("1. Adicionar/Salvar Contato")
    print("2. Ver Contatos")
    print("3. Editar Contatos")
    print("4. Favoritar/Desfavoritar Contato")
    print("5. Ver Favoritos")
    print("6. Deletar Contato")
    print("7. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_contato = input("Digite o nome do contato que deseja adicionar: ")
        telefone_contato = input("Digite o telefone deste contato: ")
        email_contato = input("Digite o email deste contato: ")
        adicionar_contatos(contatos, nome_contato, telefone_contato, email_contato)
       

    if escolha == "2":
        ver_contatos(contatos)

    if escolha =="3":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja editar: ")
        #implementar nome, telefone e email
        opcao = input("O que deseja alterar no contato: 1 - Nome, 2 - Telefone ou 3 - Email? ")
        if opcao == "1":
            novo_nome_contato = input("Digite o novo nome do contato: ")
            editar_nome_contato(contatos, indice_contato, novo_nome_contato)
        if opcao == "2":
            novo_telefone_contato = input("Digite o novo telefone do contato: ")
            editar_telefone_contato(contatos, indice_contato, novo_telefone_contato)    
        if opcao == "3":
            novo_email_contato = input("Digite o novo email do contato: ")
            editar_email_contato(contatos, indice_contato, novo_email_contato)
        else:
            print("Opção inválida!")

    if escolha == "4":
        opcao = input("O que deseja fazer? 1 - Favoritar Contato ou 2 - Desfavoritar Contato? ")
        if opcao == "1":
            ver_contatos(contatos)
            indice_contato = input("Digite o número do contato que deseja favoritar: ")
            favoritar_contato(contatos, indice_contato)
        if opcao == "2":
            ver_contatos(contatos)
            indice_contato = input("Digite o número do contato que deseja desfavoritar: ")
            desfavoritar_contato(contatos, indice_contato)
        else:
            print("Opção inválida!")

    if escolha =="5":
        ver_contato_favoritos(contatos)

    if escolha == "6":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja deletar: ")
        deletar_contato(contatos, indice_contato)
        ver_contatos(contatos)

    if escolha == "7":
        print("Programa finalizado!")
        break