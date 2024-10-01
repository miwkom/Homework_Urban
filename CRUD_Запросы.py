from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_users():
    return users


@app.post('/user/{username}/{age}')
async def post_user(username: Annotated[str,Path(min_length=4, max_length=20, description='Enter username', example='Misha')], age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]):
    user_id = str(len(users) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return {"message": f"Пользователь {user_id} успешно создан"}


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=len(users), description='Enter User ID', example='5')],
                      username: Annotated[str,Path(min_length=4, max_length=20, description='Enter username', example='Misha')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]):
    if user_id in users:
        users[user_id] = f'Имя: {username}, возраст: {age}'
        return {"message": f"Пользователь {user_id} успешно изменен"}
    else:
        return {"message": f"Пользователь с id {user_id} не найден"}


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, le=len(users), description='Enter User ID', example='5')]):
    if user_id in users:
        del users[user_id]
        return {"message": f"Пользователь {user_id} успешно удален"}
    else:
        return {"message": f"Пользователь с id {user_id} не найден"}
