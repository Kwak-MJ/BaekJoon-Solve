'''
1.아이디어
브루트포스가 된다함

시작 100번

0 ~ 9, +, - 의 리모컨

N번으로 이동
고장난 버튼의 수
고장난 버튼

원하는 채널로 이동하기 위해서 눌러야하는 버튼의 최솟값

고장난 수 제외하고 가장 인접한 수를 찾아야함

50만까지가 아니라
100만까지 브루트포스 해야함
+버튼, -버튼 모두 이용 가능하기 때문

2. 시간복잡도
2초 -> 4천만? or 2억

N = 50만
최대 nlogn

3. 예외 케이스
'''
import sys
input = sys.stdin.readline

want_cha = int(input())
err_num = int(input())
err_btn = list(map(int, input().split()))


count = abs(100 - want_cha)

# 모든 채널 체크 (브루트 포스)
for i in range(1000001):
    nums = str(i)
    for j in range(len(nums)):
        if int(nums[j]) in err_btn:
            break
        elif j == len(nums)-1:
            count = min(count, len(nums) + abs(int(nums) - want_cha))

print(count)
