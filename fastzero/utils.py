from http import HTTPStatus

from fastapi.exceptions import HTTPException


def validate_user_id(user_id, database):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found.'
        )
