import json

alunos = []
professores = []
disciplinas = []
turmas = []
matriculas = []


def exportar_para_json(lista, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo_json:
        json.dump(lista, arquivo_json)
    print(f"\nDados exportados para {nome_arquivo} com sucesso!")


def importar_de_json(nome_arquivo, lista):
    try:
        with open(nome_arquivo, 'r') as arquivo_json:
            dados = json.load(arquivo_json)
            lista.extend(dados)
        print(f"\nDados importados de {nome_arquivo} com sucesso!")
    except FileNotFoundError:
        print(f"\nArquivo {nome_arquivo} não encontrado.")


def cadastrar_aluno():
    codigo = input("\nDigite o código: ")
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")

    aluno = {'codigo': codigo, 'nome': nome, 'cpf': cpf}
    alunos.append(aluno)
    print("\nAluno cadastrado com sucesso!")


def cadastrar_professor():
    codigo = input("Digite o código: ")
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")

    professor = {'codigo': codigo, 'nome': nome, 'cpf': cpf}
    professores.append(professor)
    print("\nProfessor cadastrado com sucesso!")


def cadastrar_disciplinas():
    codigo = input("Digite o código: ")
    nome = input("Digite o nome: ")

    disciplina = {'codigo': codigo, 'nome': nome}
    disciplinas.append(disciplina)
    print("\nDisciplina cadastrada com sucesso!")


def cadastrar_turma():
    codigo_turma = input("Digite o código da turma: ")
    codigo_professor = input("Digite o código do professor: ")
    codigo_disciplina = input("Digite o código da disciplina: ")

    turma = {'codigo da turma': codigo_turma, 'codigo do professor': codigo_professor,
             'codigo da disciplina': codigo_disciplina}
    turmas.append(turma)
    print("\nTurma cadastrada com sucesso!")


def cadastrar_matricula():
    codigo_turma = input("Digite o código da turma: ")
    codigo_aluno = input("Digite o código do aluno: ")

    matricula = {'codigo da turma': codigo_turma, 'codigo do aluno': codigo_aluno}
    matriculas.append(matricula)
    print("\nMatrícula cadastrada com sucesso!")


def editar_aluno():
    codigo = input("Digite o código do aluno que deseja editar: ")

    for aluno in alunos:
        if aluno['codigo'] == codigo:
            print(f"Aluno encontrado: {aluno['nome']}")
            opcao = input("O que você deseja editar (nome ou cpf)? ").lower()
            if opcao == 'nome':
                novo_nome = input("Digite o novo nome: ")
                aluno['nome'] = novo_nome
                print("\nNome atualizado com sucesso!")
            elif opcao == 'cpf':
                novo_cpf = input("Digite o novo CPF: ")
                aluno['cpf'] = novo_cpf
                print("\nCPF atualizado com sucesso!")
            else:
                print("\nOpção inválida.")
            return

    print("\nAluno não encontrado.")


def editar_professor():
    codigo = input("Digite o código do professor que deseja editar: ")

    for professor in professores:
        if professor['codigo'] == codigo:
            print(f"Professor encontrado: {professor['nome']}")
            opcao = input("O que você deseja editar (nome ou cpf)? ").lower()
            if opcao == 'nome':
                novo_nome = input("Digite o novo nome: ")
                professor['nome'] = novo_nome
                print("\nNome atualizado com sucesso!")
            elif opcao == 'cpf':
                novo_cpf = input("Digite o novo CPF: ")
                professor['cpf'] = novo_cpf
                print("\nCPF atualizado com sucesso!")
            else:
                print("\nOpção inválida.")
            return

    print("\nprofessor não encontrado.")


def editar_disciplinas():
    codigo = input("Digite o código que deseja editar: ")

    for disciplina in disciplinas:
        if disciplina["codigo"] == codigo:
            print(f"Disciplina encontrada: {disciplina['nome']}")
            opcao_disciplina = input("Deseja editar a disciplina (s/n)? ").lower()
            if opcao_disciplina == "s":
                novo_nome = input("Digite o novo nome da disciplina: ")
                disciplina['nome'] = novo_nome
                print("Nome da disciplina atualizada com sucesso!")
            elif opcao_disciplina == "n":
                continue
            else:
                print("Opção inválida.")
            return
    print("Disciplina não encontrada.")


def editar_turma():
    codigo = input("Digite o código que deseja editar: ")

    for turma in turmas:
        if turma['codigo da turma'] == codigo:
            print(f"Turma encontrada: {turma['codigo da turma']}")
            opcao_turma = input("O que deseja editar (professor ou disciplina)? ").lower()
            if opcao_turma == "professor":
                novo_codigo = input("Digite o novo código: ")
                turma['codigo do professor'] = novo_codigo
                print("Código do professor atualizado com sucesso!")
            elif opcao_turma == "disciplina":
                novo_codigo = input("Digite o novo código: ")
                turma['codigo da disciplina'] = novo_codigo
                print("Código da disciplina atualizado com sucesso!")
            else:
                print("Opção inválida.")
            return
    print("Turma não encontrado")


def editar_matricula():
    codigo = input("Digite o código do aluno que deseja editar: ")

    for matricula in matriculas:
        if matricula["codigo do aluno"] == codigo:
            print(f"Matrícula encontrada: {matricula['codigo do aluno']}")
            opcao_matricula = input("Deseja editar a matrícula (s/n)? ").lower()
            if opcao_matricula == "s":
                novo_codigo = input("Digite o novo código da turma: ")
                matricula['codigo da turma'] = novo_codigo
                print("Matrícula atualizada com sucesso!")
            elif opcao_matricula == "n":
                continue
            else:
                print("Opção inválida.")
            return
    print("Matrícula não encontrada")


def excluir_aluno():
    codigo = input("Digite o código do aluno que deseja excluir: ")

    for aluno in alunos:
        if aluno['codigo'] == codigo:
            alunos.remove(aluno)
            print("Aluno excluído com sucesso!")
            return

    print("\nAluno não encontrado.")


def excluir_professor():
    codigo = input("Digite o código do professor que deseja excluir: ")

    for professor in professores:
        if professor['codigo'] == codigo:
            professores.remove(professor)
            print("Professor excluído com sucesso!")
            return

    print("\nProfessor não encontrado.")


def excluir_disciplina():
    codigo = input("Digite o código da disciplina que deseja excluir: ")

    for disciplina in disciplinas:
        if disciplina['codigo'] == codigo:
            disciplinas.remove(disciplina)
            print("Disciplina excluída com sucesso!")
            return

    print("\nDisciplina não encontrada.")


def excluir_turma():
    codigo_turma = input("Digite o código da turma que deseja excluir: ")

    for turma in turmas:
        if turma['codigo da turma'] == codigo_turma:
            turmas.remove(turma)
            print("Turma excluída com sucesso!")
            return

    print("\nTurma não encontrada.")


def excluir_matricula():
    codigo_aluno = input("Digite o código da matrícula que deseja excluir: ")

    for matricula in matriculas:
        if matricula['codigo do aluno'] == codigo_aluno:
            matriculas.remove(matricula)
            print("Matrícula excluída com sucesso!")
            return

    print("\nMatrícula não encontrada.")


def listar_alunos():
    if alunos:
        print("\nLista de Alunos Cadastrados:\n")
        for aluno in alunos:
            print(f"Código: {aluno['codigo']}, Nome: {aluno['nome']}, CPF: {aluno['cpf']}")
    else:
        print("\nNenhum aluno cadastrado.")


def listar_professores():
    if professores:
        print("\nLista de Professores Cadastrados:\n")
        for professor in professores:
            print(f"Código: {professor['codigo']}, Nome: {professor['nome']}, CPF: {professor['cpf']}")
    else:
        print("\nNenhum professor cadastrado.")


def listar_disciplinas():
    if disciplinas:
        print("\nLista de disciplinas Cadastradas:\n")
        for disciplina in disciplinas:
            print(f"Código: {disciplina['codigo']}, Nome: {disciplina['nome']}")
    else:
        print("\nNenhuma disciplina cadastrada.")


def listar_turmas():
    if turmas:
        print("\nLista de turmas Cadastradas:\n")
        for turma in turmas:
            print(f"Código da turma: {turma['codigo da turma']}, Código do professor: {turma['codigo do professor']},"
                  f" Código da disciplina: {turma['codigo da disciplina']}")
    else:
        print("\nNenhuma turma cadastrada.")


def listar_matriculas():
    if matriculas:
        print("\nLista de matrículas Cadastradas:\n")
        for matricula in matriculas:
            print(f"Código da turma: {matricula['codigo da turma']}, Código do aluno: {matricula['codigo do aluno']}")
    else:
        print("\nNenhuma matrícula cadastrada.")


while True:
    print("\n- = Menu principal = -\n")
    print('(1) Gerenciar alunos.')
    print('(2) Gerenciar professores.')
    print('(3) Gerenciar disciplinas')
    print('(4) Gerenciar turmas')
    print('(5) Gerenciar matrículas')
    print('(0) Sair\n')
    menu = input("informe a opção desejada: ")

    if menu == "0":
        break

    elif menu == "1":
        while True:
            print("\n[Aluno] Menu de operações:\n")
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Editar.")
            print("(4) Excluir.")
            print('(5) exportar')
            print('(6) importar')
            print("(0) Retornar ao menu principal\n")
            escolha = input("Informe a ação desejada: ")

            if escolha == '1':
                cadastrar_aluno()
            elif escolha == '2':
                listar_alunos()
            elif escolha == '3':
                editar_aluno()
            elif escolha == '4':
                excluir_aluno()
            elif escolha == '5':
                exportar_para_json(alunos, 'alunos.json')
            elif escolha == '6':
                importar_de_json('alunos.json', alunos)
            elif escolha == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")

    elif menu == "2":
        while True:
            print("\n[Professor] Menu de operações:\n")
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Editar.")
            print("(4) Excluir.")
            print('(5) exportar')
            print('(6) importar')
            print("(0) Retornar ao menu principal\n")
            escolha = input("Informe a ação desejada: ")

            if escolha == '1':
                cadastrar_professor()
            elif escolha == '2':
                listar_professores()
            elif escolha == '3':
                editar_professor()
            elif escolha == '4':
                excluir_professor()
            elif escolha == '5':
                exportar_para_json(professores, 'professores.json')
            elif escolha == '6':
                importar_de_json('professores.json', professores)
            elif escolha == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")

    elif menu == "3":
        while True:
            print("\n[Disciplina] Menu de operações:\n")
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Editar.")
            print("(4) Excluir.")
            print('(5) exportar')
            print('(6) importar')
            print("(0) Retornar ao menu principal\n")
            escolha = input("Informe a ação desejada: ")

            if escolha == '1':
                cadastrar_disciplinas()
            elif escolha == '2':
                listar_disciplinas()
            elif escolha == '3':
                editar_disciplinas()
            elif escolha == '4':
                excluir_disciplina()
            elif escolha == '5':
                exportar_para_json(disciplinas, 'disciplinas.json')
            elif escolha == '6':
                importar_de_json('disciplinas.json', disciplinas)
            elif escolha == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")

    elif menu == "4":
        while True:
            print("\n[Turma] Menu de operações:\n")
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Editar.")
            print("(4) Excluir.")
            print('(5) exportar')
            print('(6) importar')
            print("(0) Retornar ao menu principal\n")
            escolha = input("Informe a ação desejada: ")

            if escolha == '1':
                cadastrar_turma()
            elif escolha == '2':
                listar_turmas()
            elif escolha == '3':
                editar_turma()
            elif escolha == '4':
                excluir_turma()
            elif escolha == '5':
                exportar_para_json(turmas, 'turmas.json')
            elif escolha == '6':
                importar_de_json('turmas.json', turmas)
            elif escolha == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")

    elif menu == "5":
        while True:
            print("\n[Matrícula] Menu de operações:\n")
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Editar.")
            print("(4) Excluir.")
            print('(5) exportar')
            print('(6) importar')
            print("(0) Retornar ao menu principal\n")
            escolha = input("Informe a ação desejada: ")

            if escolha == '1':
                cadastrar_matricula()
            elif escolha == '2':
                listar_matriculas()
            elif escolha == '3':
                editar_matricula()
            elif escolha == '4':
                excluir_matricula()
            elif escolha == '5':
                exportar_para_json(matriculas, 'matriculas.json')
            elif escolha == '6':
                importar_de_json('matriculas.json', matriculas)
            elif escolha == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")

# fim :o)
