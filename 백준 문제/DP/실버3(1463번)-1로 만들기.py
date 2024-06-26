'''
1. 아이디어
DP인거 같음

1 -> 0번
2 -> 1번
3 -> 1번

4 -> 2번
5 -> 3번

6 -> 2번
7 -> 3번
8 -> 3번

9 -> 2번
10 -> 3번
11 -> 4번

12 ->3번
13 -> 4번
14 -> 4번

15 -> 4번
16 -> 4번
17 -> 5번

11 -> 10 -> 9 -> 3 - 1
11 -> 10 -> 5 -> 4 -> 2 -> 1

17 -> 16 -> 8 -> 4 -> 2 -> 1
17 -> 16 -> 15 -> 5 -> 4 -> 2 -> 1


4의 배수, 6의 배수, 9의 배수는 특이 케이스

우선순위가 뭐지?

1. 일단은 2, 3 배수인지 확인
2. 3의 배수이면 /3 배수의 결과 + 1
   3의 배수가 아니면서 2의 배수이면 /2 배수 결과 + 1
   
   위의 두 케이스와 바로 전의 결과 + 1 중 최솟값 선정

2. 시간 복잡도...

3. 예외 케이스
6의 배수?
3으로 바로 나누는 것보다 2로 나누는 것이
더 이득이 경우가 존재함
'''
import sys
input = sys.stdin.readline

n = int(input())
dp = [0, 0, 1, 1]

tmp = 4
while tmp <= n:
    result = []
    if tmp % 3 == 0:
        result.append(dp[tmp//3] + 1)
    if tmp % 2 == 0:
        result.append(dp[tmp//2] + 1)

    result.append(dp[tmp-1] + 1)

    dp.append(min(result))
    tmp += 1

print(dp[n])
