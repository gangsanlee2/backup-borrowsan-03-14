import random
import string
from datetime import datetime
import shortuuid

number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
first_names = ["김", "이", "박", "최", "정", "강", "조", "윤", "장", "임", "한", "오", "서", "신", "권"]
name_words = ["가", "강", "건", "경", "고", "관", "광", "구", "규", "근", "기", "길", "나", "남", "노", "누", "다", "단", "달",
              "담", "대", "덕", "도", "동", "두", "라", "래", "로", "루", "리", "마", "만", "명", "무", "문", "미", "민", "바",
              "박", "백", "범", "별", "병", "보", "빛", "사", "산", "상", "새", "서", "석", "선", "설", "섭", "성", "세", "소",
              "솔", "수", "숙", "순", "숭", "슬", "승", "시", "신", "아", "안", "애", "엄", "여", "연", "영", "예", "오", "옥",
              "완", "요", "용", "우", "원", "월", "위", "유", "윤", "율", "으", "은", "의", "이", "익", "인", "일", "잎", "자",
              "잔", "장", "재", "전", "정", "제", "조", "종", "주", "준", "중", "지", "진", "찬", "창", "채", "천", "철", "초",
              "춘", "충", "치", "탐", "태", "택", "판", "하", "한", "해", "혁", "현", "형", "혜", "호", "홍", "화", "환", "회",
              "효", "훈", "휘", "희", "운", "모", "배", "부", "림", "봉", "혼", "황", "량", "린", "을", "비", "솜", "공", "면",
              "탁", "온", "디", "항", "후", "려", "균", "묵", "송", "욱", "휴", "언", "령", "섬", "들", "견", "추", "걸", "삼",
              "열", "웅", "분", "변", "양", "출", "타", "흥", "겸", "곤", "번", "식", "란", "더", "손", "술", "훔", "반", "빈",
              "실", "직", "흠", "흔", "악", "람", "권", "복", "심", "헌", "엽", "학", "개", "롱", "평", "늘", "늬", "랑", "얀", "향",
              "울", "련"]


def lambda_fake_user(cmd):
    if cmd == "NAME":
        return lambda: ''.join(random.choice(first_names)) + ''.join(random.choices(name_words, k=2))
    elif cmd == "ID":
        return lambda: shortuuid.ShortUUID(alphabet=string.ascii_lowercase + string.digits).random(length=8)
    elif cmd == "EMAIL":
        return lambda: ''.join([''.join(random.choices(string.ascii_lowercase, k=4)), "@test.com"])
    elif cmd == "PHONE_NUMBER":
        return lambda: '-'.join(
            ['010', ''.join(random.choices(number_list, k=4)), ''.join(random.choices(number_list, k=4))])
    elif cmd == "BIRTH":
        return lambda: '-'.join(
            [str(random.randrange(1950, 2022)), str(random.randrange(1, 12)), str(random.randrange(1, 32))])
    elif cmd == "GENDER":
        return lambda: random.choice(['남성', '여성', '기타'])
    elif cmd == "ADDRESS":
        return lambda: random.choice(["서울", "경기", "부산", "대구", "광주"])


def lambda_fake_article(cmd):
    if cmd == "TITLE":
        return lambda: ''.join(random.choices(name_words, k=5))
    elif cmd == "ARTICLE_TYPE":
        return lambda: random.choice(["공지", "문의", "오류", "기타"])
    elif cmd == "CONTENT":
        return lambda: ''.join(random.choices(name_words, k=10))


def lambda_fake_rent(cmd):
    if cmd == "DATETIME":
        return lambda: datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    elif cmd == "PERCENTAGE":
        return lambda: random.randrange(0, 100)
    elif cmd == "XY":
        return lambda: random.randrange(0, 180)
    elif cmd == "STATUS":
        return lambda: random.choice(["대여전", "대여중", "수리중", "대여불가"])
    elif cmd == "URL":
        return lambda: ''.join([''.join(random.choices(string.ascii_lowercase, k=4)), ".test"])


if __name__ == '__main__':
    print("1", lambda_fake_rent("URL")())
