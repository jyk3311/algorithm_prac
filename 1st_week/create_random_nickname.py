import random

first_list = ["기철초풍", "멋있는", "재미있는"]
second_list = ["도전적인", "노란색의", "바보같은"]
third_list = ["돌고래", "개발자", "오랑우탄"]


def create_random_nickname():
    rName = ""
    rName += random.choice(first_list)
    rName += random.choice(second_list)
    rName += random.choice(third_list)

    return rName


my_nickname = create_random_nickname()
print(my_nickname)