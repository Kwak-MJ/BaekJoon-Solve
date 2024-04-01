# checkRepeat 함수
def checkRepeat(pattern):
    left = 0
    right = 1
    result = [0 for _ in range(len(pattern))]
    while right < len(pattern):
        if pattern[left] == pattern[right]:
            left += 1
            result[right] = left
            right += 1
        else:
            if left != 0:
                left = result[left - 1]
            else:
                right += 1
    return result


n = int(input())
str = list(input())
f = checkRepeat(str)

print(len(str) - f[-1])

# f[-1]이 0이면 전체 리스트가 가장 짧은 반복문
# f[-1]이 2,3,4,... 등의 정수로 끝나면, word[len(word) - f[-1]] 까지가 가장 짧은 반복문
# edge case: f[-1] 이 1로 끝나면서 앞에서 1이 반복되는 경우
# 이럴때는 f[1] 부터 1이 있는지 확인, 있다면 그 길이만큼 f[-1]에서 뒤로 간 문자열 반복
