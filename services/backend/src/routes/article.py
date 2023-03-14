from fastapi import APIRouter, Depends
from ..cruds.article import ArticleCrud
from sqlalchemy.orm import Session
from ..schemas.article import ArticleDTO
from ..database import get_db

router = APIRouter()


@router.post("/register", status_code=201)
async def register_article(dto: ArticleDTO, db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    article_crud.add_article(request_article=dto)


@router.delete("/remove", status_code=201)
async def remove_article(dto: ArticleDTO, db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    article_crud.delete_article(request_article=dto)


@router.patch("/update", status_code=201)
async def update_article(dto: ArticleDTO, db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    article_crud.update_article(request_article=dto)


@router.get("/page/{page}", status_code=201)
async def get_all_articles(dto: ArticleDTO, db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    article_crud.find_all_articles(request_article=dto)


@router.get("/id/{userid}/page/{page}", status_code=201)
async def get_articles_by_userid(article_id: str, page: int, db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    article_crud.find_articles_by_userid(article_id=article_id)


@router.get("/title/{title}/page/{page}", status_code=201)
async def get_articles_by_title(title: str, page: int, db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    article_crud.find_articles_by_title(title=title)
