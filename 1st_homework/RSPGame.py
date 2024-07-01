# **과제 내용:**
#
# 1. 플레이어와 컴퓨터가 참여하는 가위바위보 게임을 만드세요.
# 2. 게임은 다음 순서로 진행됩니다.
#     - 플레이어가 가위, 바위, 보 중 하나를 입력합니다. (done)
#     - 컴퓨터도 무작위로 가위, 바위, 보 중 하나를 선택합니다. (done)
#     - 플레이어와 컴퓨터의 선택을 비교하여 승패를 판정합니다. (done)
#     - 결과를 출력하여 플레이어가 이겼는지, 컴퓨터가 이겼는지, 비겼는지를 알려줍니다. (done)
#
# **추가 도전 과제:**
#
# 1. 게임의 승, 패, 무승부 횟수를 기록하고, 게임 종료 시에 플레이어에게 통계를 제공하세요. (done)
# 2. 플레이어가 입력할 때 대소문자를 구분하지 않도록 프로그램을 개선하세요. (done)
# 3. 플레이어가 게임을 반복하고 싶을 경우, 게임 재시작 여부를 묻고 그에 따라 게임을 초기화하거나 종료하는 기능을 추가하세요. (done)



import random
import time

computer = ['가위', '바위', '보']
win = 0
lose = 0
draw = 0
re = 'y' # 다시할건지를 확인하는 변수

#
while re == "y" or re == "Y":
    #배열이 아무렇게나 섞임. 이때 0번째 인덱스를 컴퓨터가 낸 것으로 간주
    random.shuffle(computer)
    human = input("\'가위\' \'바위\' \'보\'중에서 하나를 입력하세요: ")
    if not human in ('가위', '바위', '보'):
        print("\'가위\' \'바위\' \'보\'만 입력하세요!")
        #경고 읽을 시간주기
        time.sleep(2)
        continue

    time.sleep(0.5)
    if computer[0] == human:
        print("비겼습니다~")
        draw += 1

    #컴퓨터가 가위일 때
    elif computer[0] == '가위':
        if(human == '바위'):
            print("이겼습니다~")
            win += 1
        else:
            print("졌습니다~")
            lose += 1

    #컴퓨터가 바위일 때
    elif computer[0] == '바위':
        if(human == '보'):
            print("이겼습니다~")
            win += 1
        else:
            print("졌습니다~")
            lose += 1

    #컴퓨터가 보일 때
    elif computer[0] == '보':
        if(human == '가위'):
            print("이겼습니다~")
            win += 1
        else:
            print("졌습니다~")
            lose += 1

    time.sleep(0.5)
    print (f"컴퓨터가 낸 값: {computer[0]}")
    time.sleep(0.5)
    print (f"내가 낸 값: {human}")
    time.sleep(0.5)
    re = input("다시 하시겠습니까?(y/n): ")
    if re == "y" or re == "Y":
        continue
    elif re == "n" or re == "N":
        print("게임을 종료합니다.")
        print(f"win:{win}\tlose:{lose}\tdraw:{draw}")
        time.sleep(3)
    else:
        print("알수 없는 입력값으로 사용을 종료합니다.")