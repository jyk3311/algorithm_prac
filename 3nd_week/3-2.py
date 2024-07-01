def permute(nums):
    def backtrack(start=0):
        # 모든 숫자가 순열에 포함되었을 때 결과를 추가
        if start == len(nums):
            result.append(nums[:])
            return

        for i in range(start, len(nums)):
            # 숫자 선택
            nums[start], nums[i] = nums[i], nums[start]
            # 다음 숫자로 넘어가며 백트래킹 실행
            backtrack(start + 1)
            # 선택 취소
            nums[start], nums[i] = nums[i], nums[start]

    result = []
    backtrack()
    return result


# 예시 실행
print(permute([1, 2, 3]))