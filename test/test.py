import json
import os
from src.main import *

FILE_NAME = "tasks.json"

def test_load_tasks_file_not_exists(tmp_path, monkeypatch):
    fake_file = tmp_path / "tasks.json"

    monkeypatch.setattr("src.main.FILE_NAME", str(fake_file))

    result = load_tasks()

    assert result == []

def test_save_tasks(tmp_path, monkeypatch):
    fake_file = tmp_path / "tasks.json"

    # aponta FILE_NAME para o arquivo fake
    monkeypatch.setattr("src.main.FILE_NAME", str(fake_file))

    data = [{"task": "estudar"}, {"task": "codar"}]

    save_tasks(data)

    # verifica se o arquivo foi criado
    assert fake_file.exists()

    # verifica o conteúdo
    with open(fake_file, "r") as f:
        content = json.load(f)

    assert content == data

def test_add_task(tmp_path):
    # começa com arquivo vazio
    add_task("teste")
    # verifica se o arquivo tem 1 item com:
    {"id": 1, "task": "teste", "done": False}

def test_list_tasks_output(capsys, tmp_path):
    # cria arquivo com tarefas
    list_tasks()

    captured = capsys.readouterr()

    assert "SUAS TAREFAS" in captured.out

def test_complete_task(tmp_path, monkeypatch):
    fake_file = tmp_path / "tasks.json"

    data = [{"id": 1, "task": "teste", "done": False}]
    fake_file.write_text(json.dumps(data))

    monkeypatch.setattr("src.main.FILE_NAME", str(fake_file))

    result = complete_task(1)

    assert result is None  # ou verifica o arquivo depois

def test_complete_task_not_found(tmp_path):
    fake_file = tmp_path / "tasks.json"

    data = [
        {"id": 1, "task": "estudar", "done": False}
    ]

    fake_file.write_text(json.dumps(data))

    result = complete_task(999, fake_file)

    assert result is False

if __name__ == "__main__":
    main()