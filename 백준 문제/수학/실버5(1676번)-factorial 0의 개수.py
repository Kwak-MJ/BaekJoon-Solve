'''
1. 아이디어
math 라이브러리 사용 가능
but 그냥 해보자

while 문으로 factorial 계산

pop()을 통해 뒤에 빼주면서 0이면 count += 1
0이 아니면 끝내고 count 출력

2. 시간 복잡도
N^3 까지 가능

3. 예외 케이스
'''

n = int(input())

f_result = 1
for i in range(1, n+1):
    f_result *= i

f_result = list(str(f_result))
count = 0

while True:
    if f_result.pop() == '0':
        count += 1
    else:
        print(count)
        break


'''
빠른 풀이(문제 의도)

N이 5, 10, 15인 경우 각각 팩토리얼 시 
0이 1, 2, 3개가 나오는 규칙이 존재함

하지만 
25, 75, 100, ...
125, 250, ... 등에서 다른 갯수를 가짐을 알 수 있다.

N의 범위가 500이하이므로 5^4는 고려하지 않아도 됨
'''
n = int(input())

cnt = 0
while n > 0:
    cnt += n//5
    n //= 5

print(cnt)
