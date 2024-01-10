from fastapi import APIRouter, HTTPException, status, Response
from app.schema import createTask, updateTask
import random
from app.db import mongo_db

router = APIRouter(prefix='/task',tags=['tasks'])



@router.get('/')
def create_task():
    return {'task_data':'hello inside task'}


@router.post('/create-task',response_model=createTask)
def create_task(payload : createTask):
    payload.ChethanLReddyProperty = ''.join(random.sample('ChethanLReddyProperty',5))  
    task_data = payload.model_dump()
    task_collection = mongo_db.tasks_data
    task_data = task_collection.insert_one(task_data)
    task_data = task_collection.find_one({"_id": task_data.inserted_id})
    return task_data

@router.get('/task',response_model=list[createTask])
def alltask():
    tasks = list(mongo_db.tasks_data.find())
    if tasks is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='NOT FOUND')
    return tasks

@router.get('/task/{id}',response_model=createTask)
def gettask(id : int):
    task = mongo_db.tasks_data.find_one({"id" : id})
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='NOT FOUND')
    return task

@router.put('/updatetask/{id}',response_model=createTask)
def updatetask(id : int, payload : updateTask):
    if id != payload.id: 
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='id and task-id does not match')
    tasktoupdate = mongo_db.tasks_data.find_one({"id" : id})
    tasktoupdate_d = tasktoupdate
    tasktoupdate_d['name'] = payload.name
    tasktoupdate_d['assignee'] = payload.assignee
    tasktoupdate_d['project'] = payload.project
    tasktoupdate_d['start_time'] = payload.start_time
    result = mongo_db.tasks_data.replace_one({"id" : id},tasktoupdate_d)
    if result == 0:
        return {'message':'not updated'}
    else :
        return tasktoupdate_d

@router.delete('/deletetask/{id}',status_code=status.HTTP_204_NO_CONTENT)
def deletetask(id:int):
    result = mongo_db.tasks_data.delete_one({"id":id})
    if result is None: return {'message' : 'task not found'}
    if result.deleted_count == 1: return Response(status_code=status.HTTP_204_NO_CONTENT)
    else : return {'message' : 'task not deleted'}