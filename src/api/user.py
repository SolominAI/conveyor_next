from fastapi import APIRouter

from src.database import async_session_maker
from src.repositories.user import UserRepository
from src.schemas.user import UserAdd, UserRequestAdd

router = APIRouter(prefix='/user', tags=['Пользователь'])


@router.post("/register")
async def register_user(
        data: UserRequestAdd,
):
    hashed_password = "12345"
    new_user_data = UserAdd(email=data.email, hashed_password=hashed_password)
    async with async_session_maker() as session:
        await UserRepository(session).add(new_user_data)
        await session.commit()

    return {"status": "OK"}