from http import HTTPStatus

from fastapi import FastAPI

from fastzero.schemas import (
    Message,
    UserCreate,
    UserList,
    UserResponse,
    UserSchema,
)
from fastzero.utils import validate_user_id

app = FastAPI()
database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.post(
    '/users/', status_code=HTTPStatus.CREATED, response_model=UserResponse
)
def create_user(user: UserCreate):
    user_with_id = UserSchema(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id


@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {'users': database}


@app.put(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserResponse
)
def update_user(user_id: int, user: UserCreate):
    update_user = UserSchema(**user.model_dump(), id=user_id)

    validate_user_id(user_id=user_id, database=database)

    database[user_id - 1] = update_user

    return update_user


@app.delete('/users/{user_id}', status_code=HTTPStatus.NO_CONTENT)
def delete_user(user_id: int):
    validate_user_id(user_id=user_id, database=database)

    return database.pop(user_id - 1)
