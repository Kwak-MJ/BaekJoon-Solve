'''
1. 아이디어
range가 주어짐
1 <= i <= j <= N



2. 시간 복잡도
1초
n,m은 10만
nlogn

3. 예외 케이스
브루트포스하게 계산하면 N^2 시간이 걸림
미리 누적한 리스트를 가지고 있으면 됨
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
sff = [nums[0]]

for i in range(1, len(nums)):
    sff.append(sff[-1]+nums[i])

for _ in range(m):
    i, j = map(int, input().split())
    if i == j:
        print(nums[i-1])
    elif i == 1:
        print(sff[j-1])
    elif i != 1:
        print(sff[j-1] - sff[i-2])

