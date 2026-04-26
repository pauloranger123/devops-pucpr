import json
import os
from src.main import *

FILE_NAME = "tasks.json"

def test_load_tasks_file_not_exists(tmp_path):
    fake_file = tmp_path / "tasks.json"

    result = load_tasks(fake_file)

    assert result == []

def test_save_tasks(tmp_path):
    fake_file = tmp_path / "tasks.json"

    data = [
        {"id": 1, "task": "estudar", "done": False}
    ]

    save_tasks(data, fake_file)

    assert fake_file.exists()

    content = json.loads(fake_file.read_text())
    assert content == data

def test_add_task(tmp_path):
    # começa com arquivo vazio
    add_task("teste")
    # verifica se o arquivo tem 1 item com:
    {"id": 1, "task": "teste", "done": False}

def test_list_tasks_output(capsys, tmp_path):
    fake_file = tmp_path / "tasks.json"

    data = [
        {"id": 1, "task": "teste", "done": False}
    ]

    fake_file.write_text(json.dumps(data))

    list_tasks(fake_file)

    captured = capsys.readouterr()

    assert "teste" in captured.out

def test_complete_task(tmp_path):
    fake_file = tmp_path / "tasks.json"

    data = [
        {"id": 1, "task": "teste", "done": False}
    ]

    fake_file.write_text(json.dumps(data))

    result = complete_task(1, fake_file)

    assert result is True

def test_complete_task_not_found(tmp_path):
    fake_file = tmp_path / "tasks.json"

    data = [
        {"id": 1, "task": "teste", "done": False}
    ]

    fake_file.write_text(json.dumps(data))

    result = complete_task(999, fake_file)

    assert result is False

if __name__ == "__main__":
    main()