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
    print("\n--- SUAS TAREFAS ---")
    if not tasks:
        print("Nenhuma tarefa encontrada.")
        return
    
    for t in tasks:
        status = "[X]" if t.get("done") else "[ ]"
        print(f"{t['id']}. {status} {t['task']}")
    print("--------------------")


def complete_task(task_id):
    tasks = load_tasks()
    found = False
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            found = True
            break
    
    if found:
        save_tasks(tasks)
        print(f"\n[OK] Tarefa {task_id} marcada como concluída!")
    else:
        print(f"\n[!] Tarefa com ID {task_id} não encontrada.")

def main():
    while True:
        print("\n1. Adicionar | 2. Listar | 3. Concluir | 4. Sair")
        # .strip() remove espaços extras acidentais
        choice = input("Escolha: ").strip()
        
        if choice == "1":
            desc = input("Descrição: ").strip()
            if desc:
                add_task(desc)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_tasks()
            try:
                id_to_complete = int(input("Digite o ID da tarefa para concluir: "))
                complete_task(id_to_complete)
            except ValueError:
                print("Por favor, digite um número válido.")
        elif choice == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()