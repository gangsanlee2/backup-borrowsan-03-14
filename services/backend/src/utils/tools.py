from datetime import datetime
from pytz import timezone


def currentTime():
    today = datetime.now(timezone('Asia/Seoul'))
    return f'{today.time().strftime("%H:%M:%S")}'


def utc_seoul():
    return datetime.now(timezone('Asia/Seoul'))


from random import randrange
from datetime import timedelta


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def between_random_date():
    d1 = datetime.strptime('1988-1-1', '%Y-%m-%d')
    d2 = datetime.strptime('2005-12-31', '%Y-%m-%d')
    target = str(random_date(d1, d2))
    return target.split()[0]


def paging(request_page: int, row_cnt: int):
    page_size = 10
    t1 = row_cnt // page_size   # 몫
    t2 = row_cnt % page_size    # 나머지
    page_cnt = t1 if (t2 == 0) else t1 + 1
    block_size = 10
    t1 = page_cnt // block_size
    t2 = page_cnt % block_size
    block_cnt = t1 if (t2 == 0) else t1 + 1
    response_page = request_page -1
    row_start = page_size * response_page
    row_end = (row_cnt - 1) if page_cnt == response_page + 1 else row_start + page_size -1
    block_now = response_page // block_size
    page_start = block_now * block_size
    page_end = page_cnt - 1 if (block_cnt-1) == block_now else page_start + block_size - 1

    prev_arrow = block_now != 0
    next_arrow = block_now != block_cnt -1

    print("### 테스트 ### ")
    print(f"row_start ={row_start}")
    print(f"row_end ={row_end}")
    print(f"page_start ={page_start}")
    print(f"page_end ={page_end}")

    return {
        "row_cnt": row_cnt,
        "row_start": row_start,
        "row_end": row_end,
        "page_start": page_start,
        "page_end": page_end,
        "request_page": request_page,
        "prev_arrow": prev_arrow,
        "next_arrow": next_arrow
    }


if __name__ == '__main__':
    print(currentTime())
