#QUESTÃO 1

import random

numeros = [1,2,3,4,5] 
alunos = {}
alunos[201610040029] = "Maria Helena Pereira"
alunos[201610040023] = "Letícia Pinheiro"
alunos[201610040028] = "Maria Eduarda Martins"
mensagemProva4 = str("")
print("Seja bem vindo(a) ao Programa da Prova 4")
print("Lista:\nÉ um conjunto ordenado de valores, chamados elementos, indexados (endereçados na memória) por um índice que inicia no numeral 0, sua sintaxe é dada por colchetes [], e seu diferencial é que podemos armazenar diferentes valores dentro de apenas uma variável.\nExemplo: numeros = [1,2,3,4,5]")
print("Dicionário:\nem o mesmo princípio que a lista, uma variável armazena vários itens, porém com alguns diferenciais:\n*Sua sintaxe é dada por chaves {};\n Em apenas um elemento alocamos dois valores, um de chave, que funciona como uma espécie de índice para um valor.\nExemplo: alunos = {201610040029: Maria Helena Pereira}")
print("Estou pronto para manipular listas e dicionários na prova!")
sorteados = []
for n in range(0,21):
    s = random.choice(range(1,101))
    sorteados.append(s)
    print("O valor da linha",n,"é",s)
mensagemProva4 = "Prova sobre manipulação de listas e dicionários"
cont = len(mensagemProva4)-6
print("Número de letras armazenadas em MensagemProva4 =",cont)
mensagemProva4 = str(mensagemProva4) + ". Prova de número 4"
print(mensagemProva4)

                

