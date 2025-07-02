from fastapi import APIRouter, Body, Query

from src.api.dependencies import PaginationDep
from src.schemas.security_params import Security

router = APIRouter(prefix='/security-params', tags=['Информация о инструменте'])


@router.get('')
def get_securities(
        pagination: PaginationDep,
        id: int | None = Query(None, description="ID"),
        title: str | None = Query(None, description="Имя инструмента")
):
    # if pagination.page and pagination.per_page:
    #     return securities_[pagination.per_page*(pagination.page-1):][:pagination.per_page]
    return {'status': 'main info about all securities'}


@router.post('')
def create_security(security_data: Security = Body(openapi_examples={
    '1': {'summary': "Тестовая бумага", 'value': {
        'title': 'Тестовая бумага',
        'name': 'XXU5'
    }}
})):
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