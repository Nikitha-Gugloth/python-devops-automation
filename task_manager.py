tasks = []


def add_task(title):
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    return task


def get_tasks():
    return tasks


def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return task

    return None


def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return True

    return False


if __name__ == "__main__":

    add_task("Learn Python")
    add_task("Learn DevOps")

    print("Tasks:")
    print(get_tasks())

    complete_task(1)

    print("\nAfter completing Task 1:")
    print(get_tasks())