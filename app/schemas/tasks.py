def task_serializer(task) -> dict:
    return {
        "id": str(task["_id"]),
        "title": task["title"],
        "content": task["content"],
        "status": task["status"]
    }

def tasks_serializer(tasks) -> list:
    return [task_serializer(task) for task in tasks]
