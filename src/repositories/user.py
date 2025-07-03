from src.models.users import UsersOrm
from src.repositories.base import BaseRepository
from src.schemas.user import User


class UserRepository(BaseRepository):
    model = UsersOrm
    schema = User
    