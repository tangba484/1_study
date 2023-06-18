string = input()

# 맵(map)에 각 문자열이 몇 번 등장했는 지 기록합니다.
characters = dict()
for char in string:
    if characters.get(char, 0) == 0:
        characters[char] = 1
    else:
        characters[char] += 1

# 문자열을 오름차순 정렬하고 홀수번 등장한 문자를 기록합니다.
# 이 때 홀수번 등장한 문자가 2번 이상이면 I'm Sorry를 출력하고 종료합니다.
keys = sorted(characters.keys())
odd_char = ""
for key in keys:
    if characters.get(key) % 2 == 1:
        if odd_char == "":
            odd_char = key
        else:
            print("I'm Sorry Hansoo")
            exit(0)

# 사전순으로 문자열들을 절반 번 반복하고
# 홀수번 나오는 문자열이 있다면 이어붙이고,
# 앞쪽의 문자열을 뒤집어서 이어붙여서 팰린드롬을 만듭니다.
answer = ""
temp = ""
for key in keys:
    count = characters[key] // 2
    temp += key * count
answer += temp
if odd_char != "":
    answer += odd_char
answer += temp[::-1]

print(answer)