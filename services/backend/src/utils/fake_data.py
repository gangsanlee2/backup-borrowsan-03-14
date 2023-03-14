import random
from abc import abstractmethod

import pandas as pd
from passlib.context import CryptContext

from services.backend.src.env import engine
from services.backend.src.utils import fake_lambda

lam_user = fake_lambda.lambda_fake_user
lam_article = fake_lambda.lambda_fake_article
lam_rent = fake_lambda.lambda_fake_rent


class FakeData(object):
    @abstractmethod
    def __init__(self):
        self.table_name = ""
        self.columns = []

    @abstractmethod
    def create_record(self) -> []: pass

    def create_records(self) -> []:
        number = 10    # 생성할 레코드 수
        rows = [self.create_record() for i in range(number)]
        df = pd.DataFrame(rows, columns=self.columns)
        return df

    def insert_records(self):
        df = self.create_records()
        df.to_sql(name=self.table_name,
                  if_exists='append',
                  con=engine,
                  index=False)


class FakeUser(FakeData):
    def __init__(self):
        self.table_name = "users"
        self.columns = ['user_id', 'email', 'password', 'birth', 'gender', 'address']
        self.input_password = "12qw"

    def create_record(self) -> []:
        user_id = lam_user("ID")()
        email = lam_user("EMAIL")()
        password = CryptContext(schemes=["bcrypt"], deprecated="auto").\
            hash(self.input_password)  # 백엔드에서 실행할 경우 pip install bcrypt 필요
        birth = lam_user("BIRTH")()
        gender = lam_user("GENDER")()
        address = lam_user("ADDRESS")()
        return user_id, email, password, birth, gender, address


class FakeAdmin(FakeData):
    def __init__(self):
        self.table_name = "admins"
        self.columns = ["admin_id", "name", "password", "token"]
        self.input_password = "12qw"

    def create_record(self) -> []:
        admin_id = lam_user("ID")()
        name = lam_user("NAME")()
        password = CryptContext(schemes=["bcrypt"], deprecated="auto").\
            hash(self.input_password)
        token = None
        return admin_id, name, password, token


class FakeArticle(FakeData):
    def __init__(self):
        self.table_name = "articles"
        self.columns = ["title", "type", "text", "reference_id", "admin_id", "user_id"]

    def create_record(self) -> []:
        title = lam_article("TITLE")()
        type = lam_article("ARTICLE_TYPE")()
        text = lam_article("CONTENT")()
        reference_id = None
        admin_id = None
        user_id = None
        return title, type, text, reference_id, admin_id, user_id


class FakeRent(FakeData):
    def __init__(self):
        self.table_name = "rents"
        self.columns = ["disrepair", "rent_time", "return_time", "admin_id", "user_id", "umb_id"]

    def create_record(self) -> []:
        disrepair = lam_rent("PERCENTAGE")()
        rent_time = lam_rent("DATETIME")()
        return_time = random.choice([lam_rent("DATETIME")(), None])
        admin_id = None
        user_id = None
        umb_id = None
        return disrepair, rent_time, return_time, admin_id, user_id, umb_id


class FakeStand(FakeData):
    def __init__(self):
        self.table_name = "stands"
        self.columns = ["district", "latitude", "longitude", "admin_id"]

    def create_record(self) -> []:
        district = lam_user("ADDRESS")()
        latitude = lam_rent("XY")()
        longitude = lam_rent("XY")()
        admin_id = None
        return district, latitude, longitude, admin_id


class FakeUmbrella(FakeData):
    def __init__(self):
        self.table_name = "umbrellas"
        self.columns = ["disrepair_rate", "image_url", "status", "admin_id", "stand_id"]

    def create_record(self) -> []:
        disrepair_rate = lam_rent("PERCENTAGE")()
        image_url = lam_rent("URL")()
        status = lam_rent("STATUS")()
        admin_id = None
        stand_id = None
        return disrepair_rate, image_url, status, admin_id, stand_id


if __name__ == '__main__':
    FakeAdmin().insert_records()
    FakeUser().insert_records()
    FakeArticle().insert_records()
    FakeRent().insert_records()
    FakeStand().insert_records()
    FakeUmbrella().insert_records()
