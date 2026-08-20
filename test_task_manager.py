import task_manager


def test_add_task():
    task_manager.tasks.clear()

    task = task_manager.add_task("Learn Python")

    assert task["title"] == "Learn Python"
    assert task["completed"] is False


def test_complete_task():
    task_manager.tasks.clear()

    task_manager.add_task("Learn DevOps")

    result = task_manager.complete_task(1)

    assert result["completed"] is True


def test_delete_task():
    task_manager.tasks.clear()

    task_manager.add_task("Learn Docker")

    result = task_manager.delete_task(1)

    assert result is True
    assert len(task_manager.tasks) == 0