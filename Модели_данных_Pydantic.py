from fastapi import FastAPI, Path, status, Body, HTTPException
from pydantic import BaseModel
from typing import Annotated, List

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def get_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def post_user(
        username: Annotated[str, Path(min_length=4, max_length=20, description='Enter username', example='Misha')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]) -> User:
    new_id = len(users) + 1
    new_username = username
    new_age = age
    users.append(User(id=new_id, username=new_username, age=new_age))
    return users[-1]


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='2')],
        username: Annotated[str, Path(min_length=4, max_length=20, description='Enter username', example='Oleg')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='30')]) -> User:
    try:
        ud_user = next(user for user in users if user.id == user_id)
        ud_user.username = username
        ud_user.age = age
        return ud_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='5')]) -> User:
    try:
        for i, user in enumerate(users):
            if user.id == user_id:
                del_user = users.pop(i)
                return del_user
        raise HTTPException(status_code=404, detail="User not found")
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")
