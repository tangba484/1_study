import random
import string
from datetime import datetime, timedelta
A = ['자유게시판', '잇마이타이 봉명점', '최진엽샤브샤브', '헤이마오차이', '맛존매콤닭불고기 궁동점', '별리달리', '구들마루', '아저씨 궁동점', '상무초밥 유성점', '썸데이 제주오겹살', '한마음정육식당 대전궁동점', '원조태평소국밥', '한마음정육식당 유성봉명점', '돌돌왕십리야채곱창', '아토', '만화쉔샤오룽빠오면식관', ' 온천손칼국수쭈꾸미', '한궁양꼬치', '닭섬', '정통집 충남대점', '이순신소국밥', '경성양꼬치전문 대전본점', '누오보나폴리 궁동점', '씨멘트 충남대점', '임진강장어', '규히바치', '팬텀팬피그 궁동점 (휴업중)', '스바라시라멘 본점', '원조태평소국밥 유성점', '코니스', '황산옥', '대손관 본점', '더랜치펍', '연래춘', '로충칭마라탕 궁동점', '하루토', '동해원', '콜마르브레드', '리코타코', '바르미 샤브샤브n칼국수 봉명점', '55와인포차 본점', '연취', '작은화로', '초원돌구이', '크래버대게나라 대전유성점', '징기스 유성점']
print(A)

def random_date(start_date, end_date):
    time_difference = end_date - start_date
    random_days = random.randint(0, time_difference.days)
    return start_date + timedelta(days=random_days)

start_date = datetime(2022, 8, 1)
end_date = datetime(2023, 8, 1)



postId = 1000
posts=[]
for restaurantName in A:
    content = "test Context of PostId "
    postNum = random.randint(0,23)
    title = "test Title of PostId "
    for i in range(postNum):
        created_at = random_date(start_date, end_date)
        like_count = random.randint(0, 50)
        post_tuple = (postId, content + str(postId),str(created_at),like_count, title + str(postId), restaurantName)
        posts.append(post_tuple)
        postId += 1
print(postId)

comments=[]
commentId = 1000 + len(posts)
for p in range(1000,postId):
    date_string = str(posts[p-1000][2])
    
    formatted_date = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
    commentNum = random.randint(0,5)
    content = "test Context of CommentId "
    for i in range(commentNum):
        created_at = random_date(formatted_date, end_date)
    
        like_count = random.randint(0, 50)
        comment_tuple = (commentId, p, str(created_at), like_count, content + str(p))
        comments.append(comment_tuple)
        commentId += 1

for i in posts:
    print(i,',')
for i in comments:
    print(i,',')

# 위에서부터 코드가 이어진 상태라고 가정합니다.

# 파일에 출력 결과 저장할 경로 및 파일명 설정
output_file_path = "output.txt"

# posts 결과 저장
with open(output_file_path, "w") as output_file:
    for post_tuple in posts:
        output_file.write(str(post_tuple) + ',\n')

# comments 결과 저장
with open(output_file_path, "a") as output_file:
    for comment_tuple in comments:
        output_file.write(str(comment_tuple) + ',\n')

print("Results saved to", output_file_path)