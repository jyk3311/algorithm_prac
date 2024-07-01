import math

def lcm(a, b):
    num = int(a * b / math.gcd(a, b))
    return num

def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        answer = lcm(answer, arr[i])
    return answer

print(solution([2, 6, 8, 14]))
