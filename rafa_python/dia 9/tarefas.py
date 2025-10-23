from os import system
system("cls")

tarefas = ["Tomar café", "Lavar a louça", "Tomar banho", "Jantar"]
print(f"Lista de tarefas inicial: {tarefas}")

del tarefas[1]
print(f"Lista após remover a segunda tarefa: {tarefas}")

del tarefas[-1]
print(f"Lista após remover a última tarefa: {tarefas}")