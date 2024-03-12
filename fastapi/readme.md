| Endpoint                   | Method | Server Request                              | Server Response                              |
|----------------------------|--------|---------------------------------------------|----------------------------------------------|
| /todos/{todo_id}           | GET    | None                                        | {"title": string, "completed": boolean, "id": string} |
| /todos                     | GET    | {"title": string}                           | {"title": string, "completed": boolean, "id": string} |
| /get-by-title-and-id       | GET    | {"title": string, "id": string}             | {"title": string, "completed": boolean, "id": string} |
| /todos/get/{todo_id}       | GET    | None                                        | {"title": string, "completed": boolean, "id": string} |
| /todos/post/{todo_id}      | POST   | {"id": string, "todo": Todo item}           | {"title": string, "completed": boolean, "id": string} |
| /todos/put/{todo_id}       | PUT    | {"id": string, "todo": Todo item}           | None                                         |
| /todos/delete/{todo_id}    | DELETE | {"id": string}                              | None                                         |
