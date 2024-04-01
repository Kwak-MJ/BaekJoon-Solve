'''
아이디어
n = 1
1가지

n = 2
2가지

n = 3
3가지 

n = 4
5가지

an = a(n-1) + a(n-2)
점화식 존재
'''
i = 1  # 바로 전
j = 0  # 전의 전

n = int(input())
for _ in range(n):
    tmp = i
    i = i + j
    j = tmp

print(i % 10007)
