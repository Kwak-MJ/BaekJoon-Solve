# 아이디어: 이분탐색
# 갯수가 늘어나는 것이 절반이 기준이 되기 때문
# 긴 애의 반만 따지면 나머지는 영향 안받아?
# 어차피 계속 가운데로 조정하기 때문에, 최적의 값으로 가게 되어있음

# 처음 생각: 조건을 만족하지 않는다면 길이의 최댓값의 절반을 heapush 했음
# 이렇게 하면 1 6 / 18 처럼 절반을 했을 때 나오지 않는 길이를 출력하지 못함
# 이분탐색에서는 절반이 아니라 가운데 값이 기준이므로 항상 최적의 값 나옴
import sys

input = sys.stdin.readline

k, n = map(int, input().split())

line_len = [int(input()) for _ in range(k)]
start = 1  # 0이면 zerodivision 에러 나옴
end = max(line_len)

result = 0

while start <= end:  # 등호는?
    target = 0
    mid = (start+end) // 2

    for i in line_len:
        target += i // mid

    if target < n:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)
