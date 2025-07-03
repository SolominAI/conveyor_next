from sqlalchemy import select, func

from src.models.security_params import SecurityParamsOrm
from src.repositories.base import BaseRepository


class SecurityParamsRepositories(BaseRepository):
    model = SecurityParamsOrm

    async def get_all(
            self,
            name,
            code,
            limit,
            offset
    ):
        query = select(SecurityParamsOrm)
        if name:
            query.filter(func.lower(SecurityParamsOrm.name).contains(name.strip().lower()))
        if code:
            query.filter(func.lower(SecurityParamsOrm.code).contains(code.strip().lower()))
        query = (
            query
            .limit(limit)
            .offset(offset)
        )
        result = await self.session.execute(query)

        return result.scalars().all
