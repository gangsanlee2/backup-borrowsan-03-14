from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi_pagination import paginate, Page, Params
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse, RedirectResponse

from ..utils.tools import paging
from ..cruds.user import UserCrud
from ..database import get_db
from ..schemas.user import UserDTO, UserUpdate, UserList

router = APIRouter()

@router.post("/register", status_code=201)
async def register_user(dto: UserDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=UserCrud(db).add_user(request_user=dto)))


@router.post("/login", status_code=200)
async def login_user(dto: UserDTO, db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    token_or_fail_message = user_crud.login(request_user=dto)
    return JSONResponse(status_code=200, content=dict(msg=token_or_fail_message))


@router.post("/logout", status_code=200)
async def logout_user(dto: UserDTO, db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    token_or_fail_message = user_crud.logout(request_user=dto)
    return JSONResponse(status_code=200, content=dict(msg=token_or_fail_message))


@router.post("/load")
async def load_user(dto: UserDTO, db: Session = Depends(get_db)):
    if UserCrud(db).match_token(request_user=dto):

        return JSONResponse(status_code=200,
                            content=jsonable_encoder(
                                UserCrud(db).find_user_by_token(request_user=dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)


@router.put("/modify")
async def modify_user(dto: UserUpdate, db: Session = Depends(get_db)):
    if UserCrud(db).match_token(request_user=dto):
        return JSONResponse(status_code=200,
                            content=dict(
                                msg=UserCrud(db).update_user(dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)


@router.put("/new-password")
async def new_password(dto: UserDTO, db: Session = Depends(get_db)):
    if UserCrud(db).match_token(request_user=dto):
        return JSONResponse(status_code=200,
                            content=dict(
                                msg=UserCrud(db).update_password(dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)


@router.delete("/delete", tags=['age'])
async def remove_user(dto: UserDTO, db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    message = user_crud.delete_user(dto)
    return JSONResponse(status_code=400, content=dict(msg=message))


@router.get("/page/{page}", response_model=Page[UserList])
async def get_all_users_per_page(page: int, db: Session = Depends(get_db)):
    default_size = 5
    params = Params(page=page, size=default_size)
    results = UserCrud(db).find_all_users_ordered()
    user_info = paginate(results, params)
    count = UserCrud(db).count_all_users()
    page_info = paging(request_page=page, row_cnt=count)
    dc = {"page_info": page_info,
          "user_info": user_info}
    return JSONResponse(status_code=200, content=jsonable_encoder(dc))


@router.get("/page/{page}/size/{size}", response_model=Page[UserList])
async def get_all_users_per_page_with_size(page: int, size: int, db: Session = Depends(get_db)):
    params = Params(page=page, size=size)
    results = UserCrud(db).find_all_users_ordered()
    page_result = paginate(results, params)
    return JSONResponse(status_code=200, content=jsonable_encoder(page_result))


@router.get("/list")
async def get_all_users(db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    ls = user_crud.find_all_users()
    return {"data": ls}


@router.get("/id/{id}")
async def get_user(dto: UserDTO, db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    result = user_crud.find_user_by_id(dto)
    return result


@router.get("/email/{email}/page/{page}")
async def get_userid_by_email(dto: UserDTO, db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    user_crud.find_user_by_email(dto)
    return {"data": "success"}
