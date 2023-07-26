def get_digit_at_position(n, k):
    # 숫자의 자릿수를 찾는 함수
    def get_num_digits(num):
        digits = 0
        while num > 0:
            digits += 1
            num //= 10
        return digits

    # k번째 숫자를 찾는 함수
    def find_kth_digit(n, k):
        current_pos = 0  # 현재 위치
        for num in range(1, n + 1):
            num_digits = get_num_digits(num)
            if current_pos + num_digits >= k:
                # k번째 숫자를 찾음
                position_in_num = k - current_pos
                return int(str(num)[position_in_num - 1])

            # 다음 숫자로 이동
            current_pos += num_digits

    # k번째 숫자 반환
    if k > len(str(n * (n + 1) // 2)):
        return -1
    else:
        return find_kth_digit(n, k)

# 사용자 입력 받기
n = int(input("n을 입력하세요: "))
k = int(input("k를 입력하세요: "))

# 숫자 출력
result = get_digit_at_position(n, k)
print("결과:", result)
