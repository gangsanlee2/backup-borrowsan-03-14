from abc import ABC
from typing import List
import pymysql
from sqlalchemy.orm import Session
from ..bases.article import ArticleBase
from ..models.article import Article
from ..models.user import User
from ..schemas.article import ArticleDTO

pymysql.install_as_MySQLdb()


class ArticleCrud(ArticleBase, ABC):

    def __init__(self, db: Session):
        self.db: Session = db

    def add_article(self, request_article: ArticleDTO) -> str:
        article = Article(**request_article.dict())
        self.db.add(article)
        self.db.commit()
        return "success"

    def delete_article(self, request_article: ArticleDTO) -> str:
        article = self.find_article_by_article_id(request_article)
        is_success = self.db.query(Article).filter(Article.article_id == article.article_id).delete(synchronize_session=False)
        self.db.commit()
        return "success" if is_success != 0 else "삭제 실패입니다."

    def update_article(self, request_article: ArticleDTO) -> str:
        article = request_article.dict()
        is_success = self.db.query(Article).filter(Article.user_id == User.user_id). \
            filter(Article.article_id == article["article_id"]). \
            update({"title": article["title"], "text": article["text"]}, synchronize_session=False)
        self.db.commit()
        return "success" if is_success != 0 else "업데이트 실패"

    def find_all_articles(self, request_article: ArticleDTO) -> List[Article]:
        return self.db.query(Article).all()

    def find_articles_by_userid(self, request_article: ArticleDTO) -> List[Article]:
        article = Article(**request_article.dict())
        return self.db.query(Article).filter(Article.user_id == article.user_id).all()

    def find_articles_by_title(self, request_article: ArticleDTO) -> List[Article]:
        article = Article(**request_article.dict())
        return self.db.query(Article).filter(Article.title == article.title).all()

    def find_article_by_article_id(self, request_article: ArticleDTO) -> Article:
        article = Article(**request_article.dict())
        return self.db.query(Article).filter(Article.article_id == article.article_id).one_or_none()
