from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

# Fake database (just a list)
tasks = [
    {"id": 1, "title": "Learn CRUD", "done": False},
    {"id": 2, "title": "Build API", "done": False},
    {"id": 3, "title": "Deploy to GitHub", "done": False},
]

# GET root
@app.get("/")
def root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

# GET health
@app.get("/health")
def health():
    return {"status": "ok"}

# GET all tasks
@app.get("/tasks")
def list_tasks():
    return tasks

# GET one task
@app.get("/tasks/{id}")
def get_task(id: int):
    task = next((t for t in tasks if t["id"] == id), None)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task {id} not found")
    return task

# Data model for creating tasks
class Task(BaseModel):
    title: str

# POST new task
@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: Task):
    if not task.title or task.title.strip() == "":
        raise HTTPException(status_code=400, detail="Title is required")
    
    new_task = {
        "id": max((t["id"] for t in tasks), default=0) + 1,
        "title": task.title,
        "done": False
    }
    tasks.append(new_task)
    return new_task

# Data model for updates
class TaskUpdate(BaseModel):
    title: str = None
    done: bool = None

# PUT update task
@app.put("/tasks/{id}")
def update_task(id: int, update: TaskUpdate):
    task = next((t for t in tasks if t["id"] == id), None)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task {id} not found")
    
    if update.title is not None:
        if not update.title.strip():
            raise HTTPException(status_code=400, detail="Title cannot be empty")
        task["title"] = update.title
    
    if update.done is not None:
        task["done"] = update.done
    
    return task

# DELETE task
@app.delete("/tasks/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: int):
    global tasks
    task = next((t for t in tasks if t["id"] == id), None)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task {id} not found")
    
    tasks = [t for t in tasks if t["id"] != id]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)