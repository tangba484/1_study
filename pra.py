import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Iris 데이터셋 로드
iris = datasets.load_iris()

# 테스트 크기 매개변수 리스트 생성
test_sizes = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

# 결과 저장을 위한 리스트 초기화
scores = []

# 테스트 크기에 대한 반복문
for test_size in test_sizes:
    # 훈련 세트와 테스트 세트 생성
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=test_size, random_state=42)
    
    # KNN 알고리즘으로 훈련
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    
    # 테스트 세트로 평가 점수 계산
    score = knn.score(X_test, y_test)
    
    # 평가 점수를 리스트에 추가
    scores.append(score)

# 플롯 그리기
plt.plot(test_sizes, scores, 'o-')
plt.xlabel('Test_Size')
plt.ylabel('Score')
plt.title('Test Size vs Score')
plt.show()
