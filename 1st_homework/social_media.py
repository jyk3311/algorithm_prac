# **과제 내용:**
#
# 1. **`Member`** 클래스와 **`Post`** 클래스를 정의하세요.   (done)
# 2. **`Member`** 클래스에는 다음과 같은 속성을 가지고 있어야 합니다.   (done)
#     - 회원 이름 (**`name`**)   (done)
#     - 회원 아이디 (**`username`**)   (done)
#     - 회원 비밀번호 (**`password`**)   (done)
# 3. **`Member`** 클래스에는 다음과 같은 메소드를 가지고 있어야 합니다.   (done)
#     - 회원 정보를 print해주는 `display` (회원이름과 아이디만 보여주고 비밀번호는 보여줘서는 안됩니다!)   (done)
# 4. **`Post`** 클래스에는 다음과 같은 속성을 가지고 있어야 합니다.   (done)
#     - 게시물 제목 (**`title`**)   (done)
#     - 게시물 내용 (**`content`**)   (done)
#     - 작성자 (**`author`**) : 회원의 `username` 이 저장되어야 함!   (done)
# 5. 회원 인스턴스를 세개 이상 만들고 `members` 라는 빈리스트에 append를 써서 저장해주세요   (done)
#     1. members 리스트를 돌면서 회원들의 이름을 모두 프린트 해주세요   (done)
# 6. 각각의 회원이 게시글을 세개 이상 작성하는 코드를 만들어주세요.(회원이 세명이면 총 9개 이상의 post 인스턴스가 만들어져야 합니다).   (done)
# 만들어진 게시글 인스턴스들은 posts 빈리스트에 append를 써서 저장해주세요   (done)
#     1. for 문을 돌면서 특정유저가 작성한 게시글의 제목을 모두 프린트 해주세요   (done)
#     2. for문을 돌면서 ‘특정 단어’가 content에 포함된 게시글의 제목을 모두 프린트 해주세요   (done)


# **추가 도전 과제:**
#
# 1. input을 이용하여 Member 인스턴스 만드는것을 사용자가 터미널에서 할 수 있게 해주세요.    (done)
# 2. post도 터미널에서 생성할 수 있게 해주세요.    (done)
# 3. (심화)비밀번호 해싱이 무엇인지 공부한 후 hashlib 라이브러리를 써서 회원 비밀번호를 해시화하여 저장하게 해주세요.
#
# **평가**
#
# - 클래스와 인스턴스 개념을 설명할 수 있는가?
# - 메소드와 어트리뷰트(속성)을 설명할 수 있는가?
# - 클래스를 정의할 수 있는가?
# - 인스턴스를 생성할 수 있는가?

# ----- 코드 정의 ------
import random
import time


class Member():
    #그냥 name은 바깥에서 가져온 것. self.name은 안에 있는 것
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f"회원 이름: {self.name}")
        print(f"회원 아이디: {self.username}")



class Post:
    #author는 바깥에서 username 으로 넣어주면 됨
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


# ----- 코드 실행 ------


members = []
posts = []
#인스턴스 생성
dodo = Member("도도", "dodo", "dodo11")
rere = Member("레레", 'rere', "rere22")
mimi = Member("미미", 'mimi', "mimi33")

#members에 append
members.append(dodo)
members.append(rere)
members.append(mimi)

#member의 내장함수 display를 통해 자기자신들 출력
for member in members:
    member.display()
time.sleep(2)

#post인스턴스 생성함수
#맴버당 세번이상 작성하게 만드는 카운트 변수
do_cnt = 0
re_cnt = 0
mi_cnt = 0
#위의 카운트 변수 모두가 3을 넘기면 while문 끝남
while any([do_cnt < 4, re_cnt < 4, mi_cnt < 4]):
    i = 1
    #member리스트 섞은후 랜덤으로 글 올림
    random.shuffle(members)
    posts.append(Post(f"{i}번째글입니다.", f"{i}번째 글이어서 {i}번 반복합니다.\n" * i, members[0]))
    if members[0].name == "도도":
        do_cnt += 1
    elif members[0].name == "레레":
        re_cnt += 1
    elif members[0].name == "미미":
        mi_cnt += 1

#도도가 작성한 Post 출력
print("도도가 작성한 글들 목록")
for post in posts:
    if post.author == "도도":
        print(post.title)
time.sleep(2)

#특정 단어가 있는 게시물 제목 출력
for post in posts:
    if 1 in post.content:
        print(post.title)
time.sleep(2)

#새 맴버 받기 및 members에 넣기
new_member = input("닉네임을 입력하세요: ")
new_user_name = input("아이디를 입력하세요: ")
new_user_password = input("패스워드를 입력하세요: ")
members.append(Member(new_member, new_user_name, new_user_password))
print(f"{members[3]} 입력 완료.")

#새 포스트 작성하기
new_title = input("제목을 입력하세요: ")
new_content = input("내용을 입력하세요: ")
while True:
    new_author = input("작성자를 입력하세요: ")
    if new_author in members:
        posts.append(Post(new_title, new_content, new_author))
        print(f"{posts[-1]} 입력 완료.")
        break
    print(f"{new_author}인 가입자가 없습니다. 작성자를 다시 입력하세요.")

#해시의 의미를 알고 실습에 적용하기 위해 간단한 단방향 해시함수를 구현함
