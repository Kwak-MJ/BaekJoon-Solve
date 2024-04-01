'''
1. 아이디어
n,r,c 가 주어짐

2^n 이 한 변의 길이가 됨

특이점1: 시작이 0번째임
특이점2: 행렬을 0부터 세기 시작함

1/4를 기준으로 나누면서 갯수 세주기
가로 -> 세로 -> 전체 사이즈를 1/4로 줄임

(이 부분에서 분할정복 사용) -> 재귀로 구현가능

if r == 0 and c == 0:
~

2. 시간 복잡도
0.5초 -> 1000만
O(N)은 문제 없음

3. 주의
마지막에 1 빼주기
'''
import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

count = 0
while n > 1:
    if 2**(n-1) <= r:
        count += 2**(2*n - 1)

    if 2**(n-1) <= c:
        count += 2**(2*n - 2)

    n = n-1
    r = r % (2**n)
    c = c % (2**n)


if r == 0 and c == 0:
    count += 1
elif r == 0 and c == 1:
    count += 2
elif r == 1 and c == 0:
    count += 3
else:
    count += 4

print(count-1)


# 풀이2: 재귀
input = sys.stdin.readline

n, r, c = map(int, input().split())

count = 0


def solve(n: int, r: int, c: int):
    global count

    basis = 2**(n-1)

    if r // basis and c // basis:
        count += 3 * 2**(2*n - 2)
    elif r // basis and not c // basis:
        count += 2 * 2**(2*n - 2)
    elif not r // basis and c // basis:
        count += 1 * 2**(2*n - 2)
    else:
        pass

    if n == 1:
        return

    n = n-1
    r = r % (2**n)
    c = c % (2**n)
    solve(n, r, c)


solve(n, r, c)
print(count)
