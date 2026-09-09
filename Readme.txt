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
## AI Rematch Analysis

### Prompt Given to AI:
Build a FastAPI to-do list API:

Endpoints:
- GET / : return API info
- GET /health : return status  
- GET /tasks : return all tasks
- GET /tasks/{id} : return one task
- POST /tasks : create task (validate title)
- PUT /tasks/{id} : update task
- DELETE /tasks/{id} : delete task
- GET /stats : show total/done/open counts
- GET /tasks?search=word : search tasks
- GET /tasks?done=true : filter by done
- POST /reset : restore 3 example tasks

Status codes: 200 OK, 201 Created, 204 No Content, 400 Bad Request, 404 Not Found
In-memory list with 3 example tasks
Include Swagger UI at /docs
Use FastAPI on port 8000

### What AI Did Better:

✅ **Added Field Validation** - Used Pydantic's `Field()` with min/max length constraints. I didn't validate title length.

✅ **Task Descriptions** - Added optional description field. Gives more context to tasks.

✅ **Timestamps** - Added `created_at` to track when tasks were created. Professional feature.

✅ **Async Functions** - Used `async def` on all endpoints. Better for performance.

✅ **Type Hints & Response Models** - Defined models for requests/responses. Better code clarity.

✅ **Better Documentation** - Docstrings on every endpoint visible in Swagger UI.

### What AI Got Wrong / Added Extra:

❌ **Over-engineered** - Used `List[Task]` type hints and `response_model` which adds complexity not asked for.

❌ **Datetime Instead of Simple Objects** - Used `datetime.now()` which is more complex than needed for a learning exercise.

❌ **Global Variables** - Uses `global next_id` and `global tasks_db` which is a code smell. Could be better.

❌ **host="0.0.0.0"** - Opens to all IPs by default. Mine used `127.0.0.1` (safer for learning).

### What I Forgot to Specify:

❌ **Field Length Validation** - I didn't mention "title max 200 chars" in the prompt. AI added this.

❌ **Task Descriptions** - I only asked for id/title/done. AI added description field (good guess).

❌ **Timestamps** - I didn't specify created_at field. AI added this professionally.

❌ **Async/Await** - I didn't specify FastAPI should use async. AI made it async (correct for modern FastAPI).

### Verdict:

**AI's code is better for production.** Has validation, timestamps, documentation. But also more complex. For learning CRUD, my simpler version was fine. For real use, AI's version is professional-grade.
### What I Found:

**AI Did Better:**
- [add your findings]

**AI Got Wrong:**
- [add your findings]

**I Forgot to Specify:**
- [add your findings]
