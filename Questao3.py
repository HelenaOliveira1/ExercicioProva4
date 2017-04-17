#QUESTÃO 3

print("Recursividade:\nBasicamente funções recursivas são aquelas que se auto-chamam, ou seja, chamam a si própria dentro da sua função.")

def Atendimento(quantidade):
    if (quantidade == 0):
        print("Todas as pessoas já foram atendidas!\nExpediente encerrado!")
    else:
        print("Ainda faltam %i clientes para serem atendidos"%quantidade)
        quantidade -= 1
        Atendimento(quantidade)

quantidade = int(input("Digite quantas pessoas serão atendidas hoje: "))
Atendimento(quantidade)

print("Esta função teria serventia em um local de atendimento que possua, por exemplo, senhas de atendimento, onde só pode ser atendido aquele determinado número de pessoas.")
    
