#자판기 음료 종류 및 가격이 담긴 딕셔너리
beverages = {
		"사이다": 1700,
		"콜라": 1900,
		"식혜": 2500,
		"솔의눈": 3000
}

#자판기 이용자에게 메뉴 보여주기
for key, value in beverages.items():
    print(key + " " + str(value) + "원")

#음료 선택
user_choice = input("음료를 선택해주세요")
if not user_choice in beverages.keys():
	print("그게 뭔가요?")
	exit()

#자판기에 넣을 금액 입력
coin = input("금액을 입력해주세요")

#정수로 형변환
coin = int(coin)

#금액이 부족할 때와 잔액 출력
if coin < beverages[user_choice]:
		print("돈이 부족합니다")
		exit()
else:
	print("잔액은 " + str(coin - beverages[user_choice]) + "입니다.")