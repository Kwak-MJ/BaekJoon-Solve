'''
1. 아이디어
M, N, x, y 가 주어짐

1 <= x < M -> 다음 x = x + 1
M <= x -> 다음 x = 1

1 <= y < N -> 다음 y = y + 1
N <= y -> 다음 y = 1

유클리드 호제법 -> 최소 공배수 s 구하기
불가능한 경우: x + M * k1 <= s 까지 와 y + N * k2 <= s 안에서 같은 경우가 없을 때

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
최단시간 -> 최소 공배수 알 필요 없음, 최대범위 <= m*n 설정
            k = x 로 초기화
            if (k-x) % m == 0 and (k-y) % n == 0:
                return k
            else:
                k += m
            while문 그냥 탈출하면 return -1
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

2. 시간 복잡도
테스트 케이스 *

3. 예외 케이스
N과 M이 같다면?
N-1 까지 밖에 년도가 없음 (x=y 밖에 조합 불가)
'''
import sys

input = sys.stdin.readline

test = int(input())

for _ in range(test):
    m, n, x, y = map(int, input().split())

    # 최소 공배수 구하기
    a, b = max(m, n), min(m, n)

    while b > 0:  # 0이 되면 스탑
        a, b = b, a % b
    s = int(m * n / a)

    # 시간 초과 부분
    x_psb = [x + m * i for i in range(s // m) if (x + m * i) <= s]
    # 둘 다 가능한 리스트 만들면 시간 너무 사용
    # y_psb = [y + n*i for i in range(s//n) if (y + n*i) <= s]

    result = 0

    # y_psb 만들지 않고 x_psb for문 돌면서 나머지로 바로 확인
    for i in x_psb:
        if i < y:
            pass
        elif i == y:
            result = i
            break
        else:
            diff = i - y
            if diff % n == 0:
                result = i
                break

    if result:
        print(result)
    else:
        print(-1)