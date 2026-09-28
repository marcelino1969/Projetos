#Marcelino
#Este é um script em Python que cadastra seu nome, sua cidade e suas tarefas diárias para avaliar se a sua rotina está leve ou cheia.
nome = input("Digite seu nome: ")
cidade = input("Digite sua cidade: ")

tarefas = []
qtd = int(input("Quantas tarefas você vai cadastrar? "))

for i in range(qtd):
    tarefa = input(f"Digite a tarefa {i+1}: ")
    tarefas.append(tarefa)

print("nTarefas cadastradas:")
for t in tarefas:
    print("-", t)

if len(tarefas) == 0:
    print("Nenhuma tarefa cadastrada.")
elif len(tarefas) <= 3:
    print(f"n{nome} de {cidade}: rotina leve hoje!")
else:
    print(f"n {nome} de {cidade}: rotina cheia! Organize prioridades.")