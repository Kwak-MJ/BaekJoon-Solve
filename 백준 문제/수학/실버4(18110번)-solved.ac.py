'''
1. 아이디어
아무의견 X -> 0
의건존재 -> 모든 의견의 30%의 절사평균으로 정함(가장 큰값15%, 가장 작은값15% 제외하고 평균내기)

사람 인원수는 위, 아래에서 반올림

평균도 반올림 -> 이것이 최종 난이도

n = 의견의 개수 0부터 ~ 100,000 십만

2. 시간 복잡도
십만 -> O(NlogN)

3. 예외 케이스
아무 의견 없는 경우 처리하기
의견의 15%가 딱 안떨어질 때 반올림 처리

★ round 함수는 허점이 존재... 조심해야됨
print(round(2.5)) = 2
'''
import sys
input = sys.stdin.readline
n = int(input())


def round_num(x: float):
    if (x-int(x)) >= 0.5:
        return int(x) + 1
    else:
        return int(x)


if n == 0:
    print(0)
else:
    score = sorted([int(input()) for _ in range(n)])
    rem = round_num(n*0.15)
    score = score[rem:n-rem]
    print(round_num(sum(score) / len(score)))
