from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi_pagination import paginate, Page, Params
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse, RedirectResponse
from ..cruds.umbrella import UmbrellaCrud
from ..database import get_db
from ..schemas.umbrella import UmbrellaDTO
from ..utils.tools import paging

router = APIRouter()


@router.post("/register", status_code=201)
async def register_user(dto: UmbrellaDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=UmbrellaCrud(db).add_umbrella(request_umbrella=dto)))


@router.put("/modify")
async def modify_user(dto: UmbrellaDTO, db: Session = Depends(get_db)):
    if UmbrellaCrud(db).match_token(request_user=dto):
        return JSONResponse(status_code=200, content=dict(
                            msg=UmbrellaCrud(db).update_umbrella(dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)


@router.delete("/delete", tags=['age'])
async def remove_user(dto: UmbrellaDTO, db: Session = Depends(get_db)):
    if UmbrellaCrud(db).match_token(request_user=dto):
        return JSONResponse(status_code=200,
                            content=dict(
                                msg=UmbrellaCrud(db).delete_umbrella(dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)


@router.get("/info/{page}", response_model=Page[UmbrellaDTO])
async def get_users_per_page(page: int, db: Session = Depends(get_db)):
    results = UmbrellaCrud(db).fina_all_umbrellas()
    default_size = 5
    page_result = paginate(results, Params(page=page, size=default_size))
    print(f" ----> page_result type is {type(page_result)}")
    print(f" ----> page_result is {page_result}")
    count = UmbrellaCrud(db).count_all_umbrellas()
    pager = paging(request_page=page, row_cnt=count)
    dc = {"pager": pager,
          "users": page_result}  # items가 키값이므로 users.items
    return JSONResponse(status_code=200,
                        content=jsonable_encoder(dc))


@router.get('/info/detail/{umb_id}')
async def get_users_by_name(search: str, page: int, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=jsonable_encoder(
                            UmbrellaCrud(db).find_umbrella_by_id(search, page, db)))
