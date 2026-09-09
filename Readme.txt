# Task API

A simple to-do list API. Create, read, update, and delete tasks.

## How to Run

```bash
pip install -r requirements.txt --break-system-packages
python main.py
```

Open http://localhost:8000/docs

## Endpoints

| Method | URL | What it does |
|--------|-----|--------------|
| GET | / | API info |
| GET | /health | Server status |
| GET | /tasks | All tasks |
| GET | /tasks?done=true | Only finished tasks |
| GET | /tasks?search=CRUD | Search by title |
| GET | /tasks/{id} | One task |
| GET | /stats | Total/done/open count |
| POST | /tasks | Create task |
| PUT | /tasks/{id} | Update task |
| DELETE | /tasks/{id} | Delete task |
| POST | /reset | Restore 3 example tasks |

## Test Example

```bash
curl http://localhost:8000/tasks
curl http://localhost:8000/stats
curl http://localhost:8000/tasks?done=true
curl http://localhost:8000/tasks?search=Deploy
```

## AI Rematch

### My Prompt:
Build a FastAPI to-do list API:
- Port 8000
- In-memory list (3 example tasks)
- Task: id, title, done
- Endpoints: GET /, /health, /tasks, /tasks/{id}, POST /tasks, PUT /tasks/{id}, DELETE /tasks/{id}
- Status codes: 200 read, 201 create, 204 delete, 400 bad input, 404 not found
- Validation: title required, not empty
- Swagger UI at /docs

### What I Found:

**AI Did Better:**
- [add your findings]

**AI Got Wrong:**
- [add your findings]

**I Forgot to Specify:**
- [add your findings]