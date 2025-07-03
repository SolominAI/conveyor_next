from fastapi import APIRouter, Body, Query
from sqlalchemy import select

from src.api.dependencies import PaginationDep
from src.database import async_session_maker
from src.models.security_params import SecurityParamsOrm
from src.repositories.security_params import SecurityParamsRepositories
from src.schemas.security_params import Security, SecurityPATCH

router = APIRouter(prefix='/security-params', tags=['Информация о инструменте'])


@router.get('')
async def get_securities(
        pagination: PaginationDep,
        name: str | None = Query(None, description="Имя инструмента"),
        code: str | None = Query(None, description="Код инструмента")
):
    per_page = pagination.per_page or 5
    async with (async_session_maker() as session):
        query = select(SecurityParamsOrm)
        if name:
            query = query.filter(SecurityParamsOrm.name.like(f"%{name}%"))
        if code:
            query = query.filter(SecurityParamsOrm.code.like(f"%{code}%"))
        query = (
            query
            .limit(per_page)
            .offset(per_page * (pagination.page - 1))
        )
        result = await session.execute(query)
        securities_param = result.scalars().all()
        return securities_param


@router.get('{/security_id}')
async def get_security(security_id: int):
    async with async_session_maker() as session:
        return await SecurityParamsRepositories(session).get_one_or_none(id=security_id)


@router.post('')
async def create_security(security_data: Security = Body(openapi_examples={
    '1': {'summary': "Тестовая бумага", 'value': {
        'name': 'Тестовая бумага',
        'code': 'XXU5'
    }}
})):
    async with async_session_maker() as session:
        security = await SecurityParamsRepositories(session).add(security_data)
        await session.commit()

    return {'status': 'OK', "data": security}


@router.put('/{security_id}')
async def edit_security(
        security_id: int,
        security_data: Security = Body(openapi_examples={
            '1': {'summary': "Тестовая бумага", 'value': {
                'name': 'Тестовая бумага',
                'code': 'XXU5'
            }}
        })
):
    async with async_session_maker() as session:
        await SecurityParamsRepositories(session).edit(security_data, id=security_id)
        await session.commit()

    return {'status': 'OK'}


@router.patch('/{security_id}')
def patch_secutity(security_id: int, security_data: SecurityPATCH):
    async with async_session_maker() as session:
        await SecurityParamsRepositories(session).edit(security_data, exclude_unset=True, id=security_id)
    return {'status': 'OK'}


@router.delete('/{security_id}')
async def delete_secutity(security_id: int):
    async with async_session_maker() as session:
        await SecurityParamsRepositories(session).delete(id=security_id)
        await session.commit()
    return {'status': 'OK'}
