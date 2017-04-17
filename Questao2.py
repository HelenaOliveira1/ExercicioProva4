#QUESTÃO 2

import random 

sorteados = []
for n in range(0,21):
    s = random.choice(range(1,101))
    sorteados.append(s)
alunos = {}
alunos[201610040029] = "Maria Helena Pereira"
alunos[201610040023] = "Letícia Pinheiro"
alunos[201610040028] = "Maria Eduarda Martins"
    
def adicionarSorteado(sorteados):
    s = random.choice(range(1,101))
    sorteados.append(s)
    print(sorteados)
    main()

def adicionarAluno(alunos, matricula, nome):
    alunos[matricula] = nome
    print(alunos)
    main()

def exibirAlunos(alunos):
    print(alunos)
    main()

def buscarAlunos(alunos, matricula):
    print(alunos[matricula])
    main()

def main(Args = None):
    op = int(input("1. Adicionar sorteado\n2. adicionar Aluno\n3. Exibir Alunos\n4. Buscar Alunos\n5. Sair\n"))

    if (op == 1):
        adicionarSorteado(sorteados)
    if (op == 2):
        matricula = int(input("Digite uma matricula: "))
        nome = str(input("Digite um nome: "))
        adicionarAluno(alunos, matricula, nome)
    if (op == 3):
        exibirAlunos(alunos)
    if (op == 4):
        matricula = int(input("Digite uma matricula: "))
        buscarAlunos(alunos, matricula)
    if (op == 5):
        print("Obrigado!\nPrograma Encerrado!")
    else:
        print("OPÇÂO INVÁLIDA")
        main()
        
if (__name__ == "__main__"):
    main()
