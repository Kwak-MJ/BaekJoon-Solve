'''
1. 아이디어
듣X
보x
듣, 보 X 인 사람을 동시에 만족하는 명단 구해라

교집합 구하는 것 같음

2. 시간 복잡도
2초 => 4천만

N, M 은 50만 이하의 자연수
nlogn

3. 예외 케이스
중복 없음
소문자
띄어쓰기 없음

이중 for문은 n^2 이니 주의
문자열 stdin.readline은 rstrip 필요
'''
# 1. 대소비교를 이용한 풀이
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

listen = []
watch = []

for _ in range(n):
    listen.append(input().rstrip())

for _ in range(m):
    watch.append(input().rstrip())

listen.sort()
watch.sort()

i = 0
j = 0

result = []
while i < len(listen) and j < len(watch):
    if listen[i] == watch[j]:
        result.append(listen[i])
        i += 1
        j += 1
    elif listen[i] > watch[j]:
        j += 1
    else:
        i += 1

print(len(result))
for i in result:
    print(i)


# 2. set을 이용한 풀이
# import sys는 중복으로 생략
input = sys.stdin.readline

n, m = map(int, input().split())

listen = []
watch = []

for _ in range(n):
    listen.append(input().rstrip())

for _ in range(m):
    watch.append(input().rstrip())

result = set(listen) & set(watch)
print(result)
