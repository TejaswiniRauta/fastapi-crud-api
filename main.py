from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tasks = []

# ✅ Pydantic model (for request body)
class Task(BaseModel):
    task: str


@app.get("/")
def home():
    return {"message": "Backend is running"}


@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}


# ✅ POST using JSON body
@app.post("/tasks")
def add_task(task: Task):
    tasks.append(task.task)
    return {"message": "Task added", "tasks": tasks}


# ✅ UPDATE using JSON body
@app.put("/tasks/{index}")
def update_task(index: int, task: Task):
    if index < len(tasks):
        tasks[index] = task.task
        return {"message": "Task updated", "tasks": tasks}
    return {"error": "Task not found"}


# ✅ DELETE remains same
@app.delete("/tasks/{index}")
def delete_task(index: int):
    if index < len(tasks):
        removed = tasks.pop(index)
        return {"message": "Task deleted", "deleted": removed}
    return {"error": "Task not found"}