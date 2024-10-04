from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app_v5.backend.db_depends import get_db
from typing import Annotated
from app_v5.models.task import Task
from app_v5.models.user import User
from app_v5.schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    result = db.scalars(select(Task)).all()
    return result


@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalars(select(Task).where(Task.id == task_id)).first()
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='task not found')
    return task


@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], user_id: int, createtask: CreateTask):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
    db.execute(insert(Task).values(
        title=createtask.title,
        content=createtask.content,
        priority=createtask.priority,
        user_id=user_id,
        slug=slugify(createtask.title)
    ))
    db.commit()
    return {
       'status_code': status.HTTP_201_CREATED,
        'transaction': 'task created successfully!'
    }


@router.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, updatetask: UpdateTask):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='task not found')
    db.execute(update(task).where(task.id == task_id).values(
        title=updatetask.title,
        content=updatetask.content,
        priority=updatetask.priority,
        slug=slugify(updatetask.title)
    ))
    db.commit()
    return {
       'status_code': status.HTTP_200_OK,
        'transaction': 'task update is successful!'
    }


@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='task not found')
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'task update is successful!'
    }
