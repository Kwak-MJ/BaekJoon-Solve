'''
1. 아이디어
DP 였음
어디서 올라온건지 생각하기

n-1? or n-2?
일단 n-3 으로 가서
dp[n] = dp[n-3] + stairs[n-1] + stairs[n] 인지
dp[n] = dp[n-2] + stairs[n] 인지 생각하기
300 계단에 대해서 dp table 만들어서 생각

'''
import sys
input = sys.stdin.readline

n = int(input())
stairs = [0] * 301
for i in range(1, n+1):
    stairs[i] = int(input())

dp = [0] * 301
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1]+stairs[3], stairs[2] + stairs[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i]) # 중요 부분

print(dp[n])