def length_of_longest_substring(s):
    char_map = {}#빈 해시테이블
    start = 0#중복이 시작되는 문자의 인덱스
    maxLength = 0#최대 길이 저장하는 변수
#중복되는 문자가 나오는 순간부터 길이를 다시 재 주면서 maxLength랑 비교함.

    for i, char in enumerate(s):
        #저장된게 있고, 중복된 문자가 나오면 중복이 시작된 곳의 인덱스를 넣음
        if char in char_map and start <= char_map[char]:
            start = char_map[char] + 1
        #해시테이블에 저장된게 없으면 처음 나온 문자이므로
        else:
            maxLength = max(maxLength, i - start + 1)
        #중복되는 문자 중 제일 마지막 문자의 인덱스가 저장됨
        char_map[char] = i

    return maxLength

# 테스트
print(length_of_longest_substring("abcabcbb"))  # 출력: 3
print(length_of_longest_substring("bbbbb"))     # 출력: 1