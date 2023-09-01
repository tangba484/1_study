import random
import string
from datetime import datetime, timedelta

# 랜덤한 문자열을 생성하는 함수
def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# 랜덤한 날짜 생성
def random_date(start_date, end_date):
    time_difference = end_date - start_date
    random_days = random.randint(0, time_difference.days)
    return start_date + timedelta(days=random_days)

# 랜덤한 restaurant name 선택
restaurant_names = ["자유게시판", "아토", "아저씨 궁동점", "코니스"]

# 시작 날짜와 끝 날짜 설정
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 8, 1)

# 100개의 테스트 데이터 생성
for i in range(100):
    post_id = 100 + i
    content = f"This is the content for post {post_id}."
    created_at = random_date(start_date, end_date)
    like_count = random.randint(0, 100)
    title = f"Title for post {post_id}"
    restaurant_name = random.choice(restaurant_names)
    print(created_at)
    print(f"INSERT INTO posts (POST_ID, CONTENT, CREATED_AT, LIKE_COUNT, TITLE, RESTAURANT_NAME) VALUES ({post_id}, '{content}', '{created_at}', {like_count}, '{title}', '{restaurant_name}');")
