from fastapi import APIRouter, Body, Query
from sqlalchemy import insert, select

from src.api.dependencies import PaginationDep
from src.database import async_session_maker
from src.models.security_params import SecuritiesParamsOrm
from src.schemas.security_params import Security

router = APIRouter(prefix='/security-params', tags=['Информация о инструменте'])


@router.get('')
async def get_securities(
        pagination: PaginationDep,
        id: int | None = Query(None, description="ID"),
        name: str | None = Query(None, description="Имя инструмента"),
        code: str | None = Query(None, description="Код инструмента")
):
    per_page = pagination.per_page or 5
    async with (async_session_maker() as session):
        query = select(SecuritiesParamsOrm)
        if id:
            query = query.filter_by(id=id)
        if name:
            query = query.filter_by(name=name)
        if code:
            query = query.filter_by(code=code)
        query = (
            query
            .limit(per_page)
            .offset(per_page * (pagination.page - 1))
        )
        result = await session.execute(query)
        securities_param = result.scalars().all()
        return securities_param


@router.post('')
async def create_security(security_data: Security = Body(openapi_examples={
    '1': {'summary': "Тестовая бумага", 'value': {
        'name': 'Тестовая бумага',
        'code': 'XXU5'
    }}
})):
    async with async_session_maker() as session:
        add_security_stmt = insert(SecuritiesParamsOrm).values(**security_data.model_dump())
        await session.execute(add_security_stmt)
        await session.commit()
    return {'status': 'OK'}


@router.put('/{security_id}')
def edit_security(security_id: int, security_data: Security):
    return {'status': 'OK'}


@router.patch('/{security_id}')
def patch_secutity(security_id: int, security_data: Security):
    return {'status': 'OK'}


@router.delete('/{security_id}')
def delete_secutity(security_id: int):
    return {'status': 'OK'}