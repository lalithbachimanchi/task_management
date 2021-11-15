import datetime

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

students = []


@app.get("/")
def root():
    return {"message": "App is running!"}

taskdb = []


class TaskInput(BaseModel):
    task_name: str
    due_date: datetime.datetime


class TaskUpdateInput(BaseModel):
    task_name: str = None
    due_date: datetime.datetime = None


@app.post("/tasks", status_code=201)
def add_task(task_input: TaskInput):
    user_out_dict = {}
    user_out_dict.update(task_input)
    if len(taskdb) == 0:

        user_out_dict.update( {"task_id":1})
    else:
        user_out_dict.update({"task_id":len(taskdb) + 1})

    taskdb.append(user_out_dict)

    return user_out_dict


@app.get("/tasks", status_code=200)
def get_tasks():
    return taskdb


@app.delete("/tasks/{task_id}", status_code=200)
def get_tasks(task_id: int):

    for i in range(len(taskdb)):
        if taskdb[i]['task_id'] == task_id:
            del taskdb[i]
            break
    else:
        raise HTTPException(status_code=404, detail="Task Id not found")

    return {'message': "Task Deleted successfully"}


@app.put("/tasks/{task_id}", status_code=200)
def get_tasks(task_id: int, task_update_input: TaskUpdateInput):

    for i in range(len(taskdb)):
        if taskdb[i]['task_id'] == task_id:

            taskdb[i].update(task_update_input)
            break
    else:
        raise HTTPException(status_code=404, detail="Task Id not found")

    return {'message': "Task Updated successfully"}
