'''
1. 아이디어
+와 - 부호가 있는 경우에만 문제가 됨

최소가 되려면 
-부호 앞은 최소, 뒤는 최대가 되어야함

즉, 가장 먼저 -부호를 기준으로 나누는 과정이 필요
split('-') 이용

나머지 다 더하기

2. 시간 복잡도
2초 -> 4천만 or 2억

식의 길이 <= 50

3. 예외 케이스
0으로 시작하는 숫자 처리 필요

'''
import sys
input = sys.stdin.readline

given = input().rstrip()
given = given.split('-')


for i, num in enumerate(given):
    cnt = 0
    tmp = list(map(int, num.split('+')))
    for j in tmp:
        cnt += j
    given[i] = cnt

print(2*given[0] - sum(given))
