alunos = []
contador_matricula = {}

def gerar_matricula(curso):
    if curso not in contador_matricula:
        contador_matricula[curso] = 1
    else:
        contador_matricula[curso] += 1
    return f"{curso}{contador_matricula[curso]}"

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o e-mail do aluno: ")
    curso = input("Digite o curso do aluno (GES, GEC, GEA, etc.): ")
    matricula = gerar_matricula(curso)
    alunos.append({"nome": nome, "email": email, "curso": curso, "matricula": matricula})
    print(f"Aluno {nome} cadastrado com sucesso! Matrícula: {matricula}")

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print(f"Matrícula: {aluno['matricula']}, Nome: {aluno['nome']}, E-mail: {aluno['email']}, Curso: {aluno['curso']}")

def atualizar_aluno():
    matricula = input("Digite a matrícula do aluno a ser atualizado: ")

    for aluno in alunos:
        if aluno["matricula"] == matricula:
            print("\nAtualizando dados do aluno. Deixe em branco e pressione Enter para manter a informação atual.")

            novo_nome = input("Digite o novo nome: ")
            if novo_nome:
                aluno["nome"] = novo_nome

            novo_email = input("Digite o novo e-mail: ")
            if novo_email:
                aluno["email"] = novo_email

            novo_curso = input("Digite o novo curso: ")
            if novo_curso:
                aluno["curso"] = novo_curso

            print("Aluno atualizado com sucesso!")
            return
    print("Aluno não encontrado.")

def remover_aluno():
    matricula = input("Digite a matrícula do aluno a ser removido: ")
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            alunos.remove(aluno)
            print("Aluno removido com sucesso!")
            return
    print("Aluno não encontrado.")

def main():
    while True:
        print("\nMenu de Opções:")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Remover Aluno")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            atualizar_aluno()
        elif opcao == '4':
            remover_aluno()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
