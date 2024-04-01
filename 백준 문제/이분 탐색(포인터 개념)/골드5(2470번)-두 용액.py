# -99 -2 -1 4 98
# 알칼리성 -10억 ~ -1
# 산성 1 ~ 10억
# 투포인터로 두 수의 합의 절댓값이 가장 작은 조합 찾으면 바로 return

def minFromO(value: list):
    left = 0
    right = len(value) - 1
    min_sum = 2*10e9
    result = [value[left], value[right]]
    if value[0] < 0 and value[-1] < 0:
        result = [value[-2], value[-1]]
        return result
    elif value[0] > 0 and value[-1] > 0:
        result = [value[0], value[1]]
        return result
    else:
        while left < right:
            current_sum = value[left] + value[right]
            if current_sum == 0:
                result = [value[left], value[right]]
                return result

            if abs(current_sum) <= min_sum:
                min_sum = abs(current_sum)
                result = [value[left], value[right]]

            if current_sum < 0:
                left += 1
            else:
                right -= 1

        return result


sol_nums = int(input())
value = list(map(int, input().split()))
value.sort()

answer = minFromO(value)
print(answer[0], answer[1])
