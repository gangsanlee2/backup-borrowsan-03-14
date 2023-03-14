from abc import ABC
from typing import List

from sqlalchemy.orm import Session

from ..bases.admin import AdminBase
from ..models.admin import Admin
from ..schemas.admin import AdminDTO
from ..utils.security import myuuid, get_hashed_password, verify_password, generate_token


class AdminCrud(AdminBase, ABC):

    def __init__(self, db: Session):
        self.db: Session = db

    def add_admin(self, request_admin: AdminDTO) -> str:
        admin_dict = Admin(**request_admin.dict())
        admin_id = self.find_admin_by_name(request_admin=request_admin)
        if admin_id == "":
            admin_dict.admin_id = myuuid()
            admin_dict.password = get_hashed_password(admin_dict.password)
            is_success = self.db.add(admin_dict)
            self.db.commit()
            self.db.refresh(admin_dict)
            message = "SUCCESS: 회원가입이 완료되었습니다" if is_success != 0 else "FAILURE: 회원가입이 실패하였습니다"
        else:
            message = "FAILURE: 이름이 이미 존재합니다"
        return message

    def login(self, request_admin: AdminDTO) -> str:
        admin_id = self.find_admin_by_name(request_admin=request_admin)
        print("login 시작")
        if admin_id != "":
            request_admin.admin_id = admin_id
            db_admin = self.find_admin_by_id(request_admin)
            verified = verify_password(plain_password=request_admin.password,
                                       hashed_password=db_admin.password)
            if verified:
                new_token = generate_token(request_admin.name)
                request_admin.token = new_token
                self.update_token(db_admin, new_token)
                return new_token
            else:
                return "FAILURE: 비밀번호가 일치하지 않습니다"
        else:
            return "FAILURE: 아이디가 존재하지 않습니다"

    def logout(self, request_admin: AdminDTO) -> str:
        admin = self.find_admin_by_token(request_admin)
        is_success = self.db.query(Admin).filter(Admin.admin_id == admin.admin_id).update({Admin.token: ""})
        self.db.commit()
        return "로그아웃 성공입니다." if is_success != 0 else "로그아웃 실패입니다."

    def update_token(self, db_admin: Admin, new_token: str) -> str:
        is_success = self.db.query(Admin).filter(Admin.admin_id == db_admin.admin_id) \
            .update({Admin.token: new_token}, synchronize_session=False)
        self.db.commit()
        self.db.refresh(db_admin)
        return "success" if is_success != 0 else "failed"

    def update_password(self, request_admin: AdminDTO) -> str:
        admin = Admin(**request_admin.dict())
        admin.password = get_hashed_password(admin.password)
        is_success = self.db.query(Admin).filter(Admin.token == admin.token) \
            .update({Admin.password: admin.password}, synchronize_session=False)
        self.db.commit()
        return "success" if is_success != 0 else "failed"

    def delete_admin(self, request_admin: AdminDTO) -> str:
        admin = self.find_admin_by_id(request_admin)
        is_success = self.db.query(Admin).filter(Admin.admin_id == admin.admin_id).delete(synchronize_session=False)
        self.db.commit()
        return "탈퇴 성공입니다." if is_success != 0 else "탈퇴 실패입니다."

    def find_all_admins_ordered(self) -> List[Admin]:
        return self.db.query(Admin).order_by(Admin.created_at).all()

    def find_admin_by_token(self, request_admin: AdminDTO) -> Admin:
        admin = Admin(**request_admin.dict())
        return self.db.query(Admin).filter(Admin.token == admin.token).one_or_none()

    def find_admin_by_id(self, request_admin: AdminDTO) -> Admin:
        print("find_admin_by_id 진입")
        admin = Admin(**request_admin.dict())
        print("find_admin_by_id 리턴 전")
        print("리턴 전 필터 값", self.db.query(Admin).filter(Admin.admin_id == admin.admin_id).one_or_none())
        return self.db.query(Admin).filter(Admin.admin_id == admin.admin_id).one_or_none()

    def find_all_admins(self) -> List[Admin]:
        return self.db.query(Admin).all()

    def match_token(self, request_admin: AdminDTO) -> bool:
        admin = Admin(**request_admin.dict())
        db_admin = self.db.query(Admin).filter(Admin.token == admin.token).one_or_none()
        return True if db_admin != None else False

    def find_admin_by_name(self, request_admin: AdminDTO) -> str:
        admin = Admin(**request_admin.dict())
        db_admin = self.db.query(Admin).filter(Admin.name == admin.name).one_or_none()
        if db_admin is not None:
            return db_admin.admin_id
        else:
            return ""

