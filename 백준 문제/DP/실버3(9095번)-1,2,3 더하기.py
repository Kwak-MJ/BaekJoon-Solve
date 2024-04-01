'''
1. 아이디어
정수 n 을
1,2,3의 자연수 합으로 나타내기 (1개 이상)

2. 시간 복잡도
n이 11보다 작음
브루트포스하게도 될 것 같음
dp도 되나?

3. 예외 케이스
순서 차등

n = 1 1개
n = 2 1+1, 2 2개
n = 3 1+1+1, 1+2, 2+1, 3 4개
n = 4 1+1+1+1, 2+1+1, 1+2+1, 1+1+2, 2+2, 1+3, 3+1 7개
n = 5 
1+1+1+1+1
2+1+1+1, 1+2+1+1, 1+1+2+1, 1+1+1+2
1+2+2, 2+1+2, 2+2+1
1+1+3, 1+3+1, 3+1+1
1+4, 4+1 #
2+3, 3+2
15개 - 2 = 13개

n = 6
111111 -> 1개
11112 -> 5개
1122 -> 6개
222 -> 1개
1113 -> 4개
33 -> 1개
123 -> 6개
23개    

an = a(n-1) + a(n-2) + a(n-3)

n=7
63 - 19개 = 44개
'''
import sys
input = sys.stdin.readline

test = int(input())
dp_table = [0, 1, 2, 4]

for _ in range(test):
    n = int(input())

    while len(dp_table) <= n:
        dp_table.append(dp_table[-1] + dp_table[-2] + dp_table[-3])

    print(dp_table[n])
