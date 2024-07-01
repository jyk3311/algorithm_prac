#랜덤한 것을 코딩할 때 포함되는 라이브러리
import random

#기회
count = 9

#사용자가 내놓는 추측
guess = ""

#프로그램 안에 있는 단어들
word= [
    "airplane",
    "apple",
    "arm",
    "bakery",
    "banana",
    "bank",
    "bean",
    "belt",
    "bicycle",
    "biography",
    "blackboard",
    "boat",
    "bowl",
    "broccoli",
    "bus",
    "car",
    "carrot",
    "chair",
    "cherry",
    "cinema",
    "class",
    "classroom",
    "cloud",
    "coat",
    "cucumber",
    "desk",
    "dictionary",
    "dress",
    "ear",
    "eye",
    "fog",
    "foot",
    "fork",
    "fruits",
    "hail",
    "hand",
    "head",
    "helicopter",
    "hospital",
    "ice",
    "jacket",
    "kettle",
    "knife",
    "leg",
    "lettuce",
    "library",
    "magazine",
    "mango",
    "melon",
    "motorcycle",
    "mouth",
    "newspaper",
    "nose",
    "notebook",
    "novel",
    "onion",
    "orange",
    "peach",
    "pharmacy",
    "pineapple",
    "plate",
    "pot",
    "potato",
    "rain",
    "shirt",
    "shoe",
    "shop",
    "sink",
    "skateboard",
    "ski",
    "skirt",
    "sky",
    "snow",
    "sock",
    "spinach",
    "spoon",
    "stationary",
    "stomach",
    "strawberry",
    "student",
    "sun",
    "supermarket",
    "sweater",
    "teacher",
    "thunderstorm",
    "tomato",
    "trousers",
    "truck",
    "vegetables",
    "vehicles",
    "watermelon",
    "wind"
]

#리스트 요소 랜덤하게 뽑기
temp = random.choice(word)

#뽑은 요소 한글자씩 리스트화 시키기
answer = list(temp)

guessing_answer = []
for i in range(len(temp)):
    guessing_answer.append('_')

while count != 0:
    print("현재 남은 기회 : " + str(count))
    guess = input("A-Z 중 하나를 입력하세요 ")

    #여러개 입력할 경우
    if len(guess) > 1:
        print("하!나!만! 입력하세요. 기회가 1 차감됩니다.")
        count -= 1
        continue

    #대문자까지는 허용 -> 소문자로 변환
    if 'A' <= guess <= 'Z':
        guess = guess.lower()

    #정답이 있는 경우
    if 'a' <= guess <= 'z':
        for i, ans in enumerate(answer):
            if guess == ans:
                guessing_answer[i] = guess
                print(i)
        count -= 1
        print(guessing_answer)
        if answer == guessing_answer:
            print("정답입니다! ", guessing_answer)
            exit()
    #잘못 입력한 경우
    else:
        print("정답에 포함된 알파벳이 아닙니다. 기회가 1 차감됩니다.")
        count -= 1