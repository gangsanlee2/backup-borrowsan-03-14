from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi_pagination import paginate, Page, Params
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from ..cruds.rent import RentCrud
from ..database import get_db
from ..schemas.rent import RentDTO
from ..utils.tools import paging

router = APIRouter()


@router.get("/info/{page}", response_model=Page[RentDTO])
async def get_users_per_page(page: int, db: Session = Depends(get_db)):
    results = RentCrud(db).fina_all_rents()
    default_size = 5
    page_result = paginate(results, Params(page=page, size=default_size))
    print(f" ----> page_result type is {type(page_result)}")
    print(f" ----> page_result is {page_result}")
    count = RentCrud(db).count_all_rents()
    pager = paging(request_page=page, row_cnt=count)
    dc = {"pager": pager,
          "users": page_result}  # items가 키값이므로 users.items
    return JSONResponse(status_code=200,
                        content=jsonable_encoder(dc))
