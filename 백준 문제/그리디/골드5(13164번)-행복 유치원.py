# 아이디어
# 가장 긴 간격부터 차례대로 빼주기
# 마지막 순서에는 나머지 모두 더하기

n, k = map(int, input().split())

tall = list(map(int, input().split()))
tall_diff = []
for i in range(len(tall)-1):
    tall_diff.append(tall[i+1] - tall[i])

tall_diff.sort()

result = []
for i in range(k):
    if i == k-1:
        result.append(sum(tall_diff))
    else:
        tall_diff.pop()
        result.append(0)

print(sum(result))
