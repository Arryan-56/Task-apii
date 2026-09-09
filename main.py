from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

# Fake database
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

# GET stats
@app.get("/stats")
def stats():
    return {
        "total": len(tasks),
        "done": len([t for t in tasks if t["done"]]),
        "open": len([t for t in tasks if not t["done"]])
    }

# GET all tasks (with filter + search)
@app.get("/tasks")
def list_tasks(done: bool = None, search: str = None):
    result = tasks
    
    if done is not None:
        result = [t for t in result if t["done"] == done]
    
    if search:
        result = [t for t in result if search.lower() in t["title"].lower()]
    
    return result

# GET one task
@app.get("/tasks/{id}")
def get_task(id: int):
    task = next((t for t in tasks if t["id"] == id), None)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task {id} not found")
    return task

# Task model
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

# Update model
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

# POST reset
@app.post("/reset")
def reset_tasks():
    global tasks
    tasks = [
        {"id": 1, "title": "Learn CRUD", "done": False},
        {"id": 2, "title": "Build API", "done": False},
        {"id": 3, "title": "Deploy to GitHub", "done": False},
    ]
    return {"message": "Tasks reset"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)