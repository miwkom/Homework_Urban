from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app_v4.backend.db_depends import get_db
from typing import Annotated
from app_v4.models.user import User
from app_v4.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix='/user', tags=['user'])


@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    result = db.scalars(select(User)).all()
    return result


@router.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalars(select(User).where(User.id == user_id)).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return user


@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], createuser: CreateUser):
    db.execute(insert(User).values(username=createuser.username,
                                   firstname=createuser.firstname,
                                   lastname=createuser.lastname,
                                   age=createuser.age,
                                   slug=slugify(createuser.username)))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


@router.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, updateuser: UpdateUser):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    db.execute(update(User).where(User.id == user_id).values(
        firstname=updateuser.firstname,
        lastname=updateuser.lastname,
        age=updateuser.age
    ))
    db.commit()
    return {
       'status_code': status.HTTP_200_OK,
        'transaction': 'User update is successful!'
    }


@router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    db.execute(delete(User).where(User.id == user_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User update is successful!'
    }
