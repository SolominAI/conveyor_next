from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class SecuritiesParamsOrm(Base):
    __tablename__ = "securities_param"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    code: Mapped[str] = mapped_column(String(10))

