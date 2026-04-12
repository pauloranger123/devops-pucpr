import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"id": len(tasks) + 1, "task": description, "done": False})
    save_tasks(tasks)
    print(f"Tarefa adicionada: {description}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Nenhuma tarefa pendente.")
        return
    for t in tasks:
        status = "[X]" if t["done"] else "[ ]"
        print(f"{t['id']}. {status} {t['task']}")

def main():
    while True:
        print("\n--- To-Do List CLI ---")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            desc = input("Descrição da tarefa: ")
            add_task(desc)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()