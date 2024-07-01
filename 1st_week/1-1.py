def solution(sentence):
    for i in range(len(sentence) // 2):
        if sentence[i] != sentence[-(i+1)]:
            return False
    return True


print(solution("ratar"))
print(solution("avttva"))
print(solution("abcdbba"))

