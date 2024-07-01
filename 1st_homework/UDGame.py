# **내용:**
#
# 1. 플레이어와 컴퓨터가 참여하는 업다운 게임을 만드세요.
# 1. 프로그램은 다음과 같은 기능을 포함해야 합니다.
#     - 컴퓨터는 1부터 100 사이의 랜덤한 숫자를 생성합니다.  (done)
#     - 플레이어는 숫자를 입력하고, 입력한 숫자와 컴퓨터의 숫자를 비교하여 "업" 또는 "다운" 힌트를 제공합니다.  (done)
#     - 플레이어가 컴퓨터의 숫자를 정확히 맞히면 시도한 횟수를 알려줍니다.  (done)
#     - 플레이어가 숫자를 맞힐 때까지 위 과정을 반복합니다.  (done)
#
# **추가 도전 과제:**
#
# 1. 플레이어가 입력한 숫자가 범위를 벗어날 경우, 적절한 안내 메시지를 출력하여 유효한 범위 내의 숫자를 입력하도록 유도하세요.  (done)
# 2. 플레이어가 게임을 반복하고 싶을 경우, 게임 재시작 여부를 묻고 그에 따라 게임을 초기화하거나 종료하는 기능을 추가하세요.  (done)
# 3. 게임이 종료될 때 플레이어의 최고 시도 횟수를 기록하고, 다음 게임에서 이를 표시하는 기능을 구현하세요.


import random
import time

import numpy as np

computer = np.random.randint(1, 101)
player = 0
count = 0
is_first_time = True
best_score = 0
while True:
    #시도 횟수
    count += 1
    #숫자를 입력 안했을 때
    try:
        player = int(input("숫자를 입력하세요: "))
    except ValueError:
        print("숫!자!를 입력하세요.")
        time.sleep(2)
        continue

    #1~100안으로 입력을 안했을 때
    if player < 1 or player > 100:
        print("유효한 범위 내의 숫자를 입력하세요.(1 ~ 100)")
        time.sleep(2)
        continue

    #입력한 숫자가 정답보다 클 때
    if player > computer:
        print("다운")
        time.sleep(0.5)
    #입력한 숫자가 정답보다 작을 때
    elif player < computer:
        print("업")
        time.sleep(0.5)
    #정답
    else:
        print("맞았습니다.")
        time.sleep(0.5)
        print(f"시도한 횟수: {count}")
        #처음이면 지금 시도한 횟수 best_score에 넣기
        if is_first_time:
            is_first_time = False
            best_score = count
        if best_score > count:
            best_score = count
        time.sleep(1)
        print(f"이번 게임에서 제일 빠르게 맞친 횟수: {best_score}")
        time.sleep(1.5)
        re = input("다시 하시겠습니까? (y/n): ")
        #다시한다면 랜덤한 숫자 다시 받고 count 초기화
        if re == "y" or re == "Y":
            #처음이 아닌데 best_score보다 시도 횟수가 작으면 교체
            computer = np.random.randint(1, 101)
            count = 0
            time.sleep(0.5)
            continue
        #끝내기 while문 탈출
        elif re == "n" or re == "N":
            print("게임을 종료합니다.")
            time.sleep(2)
            break
        #비정상 종료로 exit code에 -1 보내기
        else:
            print("알수 없는 입력값으로 사용을 종료합니다.")
            time.sleep(1)
            exit(-1)

