parking = ["가능"]*10

cnt = 10 # 주차 가능 공간

while True:
    state = input("입차를 원하시면 0 , 출차를 원하시면 1을 입력해주세요")

    if state == "0":
        
        print(parking)
        if cnt == 0:
            print("FULL")
            continue
        while 1:
            n = int(input("원하시는 주차 공간을 알려주세요"))
            if parking[n-1] == "불가":
                print("빈 주차 공간을 선택해주세요")
                continue
            else:
                break
        parking[n-1] = "불가"
        cnt -= 1
    else:
        if cnt == 10:
            print("주차 되어있는 차가 없습니다")
            continue
        n = int(input("주차를 한 구역의 번호를 입력해주세요"))
        parking[n-1] = "가능"
        cnt += 1
        