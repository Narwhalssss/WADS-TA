from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class TodoItem(BaseModel):
    title: str
    completed: bool
    id: str


todos = {}

@app.get("/todos/get/{todo_id}")
def get_todo_by_id(todo_id: str):
    if todo_id not in todos:
        return {"Error": f"Todo ID {todo_id} not found."}
    return todos[todo_id]

@app.get("/todos")
def get_todo_by_title(title: Optional[str] = None):
    for todo_id in todos:
        if todos[todo_id]["title"] == title:
            return todos[todo_id]
    return {"Error": f"Todo with title '{title}' not found."}

@app.get("/get-by-title-and-id")
def get_by_title_and_id(title: str, id: str):
    if id in todos and todos[id]["title"] == title:
        return todos[id]
    return {"Error": f"Todo with ID {id} and title '{title}' not found."}

@app.post("/todos/post/{todo_id}")
def post_todo(todo_id: str, todo: TodoItem):
    if todo_id in todos:
        return {"Error": f"Todo ID {todo_id} already exists."}
    todos[todo_id] = todo.dict()
    return todos[todo_id]

@app.put("/todos/put/{todo_id}")
def put_todo(todo_id: str, todo: TodoItem):
    if todo_id not in todos:
        return {"Error": f"Todo ID {todo_id} not found."}
    todos[todo_id] = todo.dict()
    return {"message": f"Todo ID {todo_id} updated."}

@app.delete("/todos/delete/{todo_id}")
def delete_todo(todo_id: str):
    if todo_id not in todos:
        return {"Error": f"Todo ID {todo_id} not found."}
    del todos[todo_id]
    return {"message": f"Todo ID {todo_id} deleted."}