from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi_pagination import paginate, Params
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse, RedirectResponse

from ..cruds.admin import AdminCrud
from ..database import get_db
from ..schemas.admin import AdminDTO
from ..utils.tools import paging

router = APIRouter()


@router.post("/register", status_code=201)
async def register_admin(dto: AdminDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=AdminCrud(db).add_admin(request_admin=dto)))


@router.post("/login", status_code=200)
async def login_admin(dto: AdminDTO, db: Session = Depends(get_db)):
    admin_crud = AdminCrud(db)
    token_or_fail_message = admin_crud.login(request_admin=dto)
    return JSONResponse(status_code=200, content=dict(msg=token_or_fail_message))


@router.post("/logout", status_code=200)
async def logout_admin(dto: AdminDTO, db: Session = Depends(get_db)):
    admin_crud = AdminCrud(db)
    token_or_fail_message = admin_crud.logout(request_admin=dto)
    return JSONResponse(status_code=200, content=dict(msg=token_or_fail_message))


@router.post("/load")
async def load_admin(dto: AdminDTO, db: Session = Depends(get_db)):
    if AdminCrud(db).match_token(request_admin=dto):
        return JSONResponse(status_code=200,
                            content=jsonable_encoder(
                                AdminCrud(db).find_admin_by_token(request_admin=dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)


@router.put("/new-password")
async def new_password(dto: AdminDTO, db: Session = Depends(get_db)):
    if AdminCrud(db).match_token(request_admin=dto):
        return JSONResponse(status_code=200,
                            content=dict(
                                msg=AdminCrud(db).update_password(dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)


@router.delete("/delete", tags=['age'])
async def remove_admin(dto: AdminDTO, db: Session = Depends(get_db)):
    admin_crud = AdminCrud(db)
    message = admin_crud.delete_admin(dto)
    return JSONResponse(status_code=400, content=dict(msg=message))


@router.get("/page/{page}")
async def get_all_admins_per_page(page: int, db: Session = Depends(get_db)):
    default_size = 5
    params = Params(page=page, size=default_size)
    results = AdminCrud(db).find_all_admins_ordered()
    admin_info = paginate(results, params)
    count = admin_info.dict()['total']
    page_info = paging(request_page=page, row_cnt=count)
    dc = {"page_info": page_info,
          "user_info": admin_info}
    return JSONResponse(status_code=200, content=jsonable_encoder(dc))


@router.get("/show")
async def all_show(db: Session = Depends(get_db)):
    results = AdminCrud(db).find_all_admins_ordered()
    return JSONResponse(status_code=200, content=jsonable_encoder(results))


@router.get("/page/{page}/size/{size}")
async def get_all_admins_per_page_with_size(page: int, size: int, db: Session = Depends(get_db)):
    params = Params(page=page, size=size)
    results = AdminCrud(db).find_all_admins_ordered()
    page_result = paginate(results, params)
    return JSONResponse(status_code=200, content=jsonable_encoder(page_result))


@router.get("/list")
async def get_all_admins(db: Session = Depends(get_db)):
    admin_crud = AdminCrud(db)
    ls = admin_crud.find_all_admins()
    return {"data": ls}


@router.get("/id/{id}")
async def get_admin(dto: AdminDTO, db: Session = Depends(get_db)):
    admin_crud = AdminCrud(db)
    result = admin_crud.find_admin_by_id(dto)
    return result


@router.get("/name/{name}/page/{page}")
async def get_admin_id_by_name(dto: AdminDTO, db: Session = Depends(get_db)):
    admin_crud = AdminCrud(db)
    admin_crud.find_admin_by_name(dto)
    return {"data": "success"}
