# in 을 연산할 때 set과 list에서의 시간 복잡도가 다른 것을 이해

n, m = map(int, input().split())
strs = set()
count = 0

# n에 속하는 문자열 입력받고, 집합에 추가
for _ in range(n):
    strs.add(input())


# m에 속하는 문자열 입력받고 strs 집합에 있는지 확인하기
for _ in range(m):
    if input() in strs:
        count += 1

# set을 이용하여 같은 문자열 생략, strs의 총 길이는 (n+m-(같은 문자열 개수))
print(count)
