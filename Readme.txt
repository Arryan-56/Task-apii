# Task API

A simple to-do list API. You can create, read, update, and delete tasks.

## How to Run

1. Install Python
2. Download this repo
3. Run this command:

```bash
pip install -r requirements.txt --break-system-packages
python main.py
```

4. Open http://localhost:8000/docs in your browser
5. You can now create, edit, and delete tasks

## API Endpoints

| Method | URL | What it does |
|--------|-----|--------------|
| GET | /tasks | Get all tasks |
| GET | /tasks/1 | Get task 1 |
| POST | /tasks | Create new task |
| PUT | /tasks/1 | Update task 1 |
| DELETE | /tasks/1 | Delete task 1 |

## Testing Example

```bash
curl http://localhost:8000/tasks
```

This returns all your tasks as JSON.

## Swagger UI

Go to http://localhost:8000/docs

You can test all endpoints there with buttons. No terminal needed.