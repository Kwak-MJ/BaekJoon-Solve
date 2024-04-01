'''
1. 아이디어
구현은 안어려움
시간초과 고려해서 딕셔너리 사용

2. 시간 복잡도
딕셔너리 구현에만 N 타임 소요
불러오는 것 m 타임

'''
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

num_name = dict()
name_num = dict()

for i in range(n):
    name = input().rstrip()
    num_name[i+1] = name
    name_num[name] = i+1

for _ in range(m):
    test = input().rstrip()
    if test.isdigit():
        print(num_name[int(test)])
    else:
        print(name_num[test])
