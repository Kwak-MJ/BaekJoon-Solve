'''
1. 아이디어
테스트는 최대 100

수행 할 함수를 한줄로 입력받음
RDD
for 문을 통해 문자열 읽어오기 실행 -> 10만번

if 문으로 R인지 D 인지 체크

정수 배열을 따로 만들고
D 연산인 경우는 길이 체크

2. 시간 복잡도

3. 예외
배열이 비어있는 경우 D 연산은 -> error 출력

배열이 비어있는 경우 R 연산은 괜찮나?
'''
import sys
from collections import deque

input = sys.stdin.readline

test = int(input())
for _ in range(test):
    order = input().rstrip()
    n = int(input())

    arr = input().rstrip()
    arr = deque(arr[1:len(arr)-1].split(','))

    result = True
    reverse = False

    for char in order:
        if char == 'R':
            reverse = not reverse
        elif char == 'D':
            if n == 0:
                result = False
                break
            else:
                if reverse:
                    arr.pop()
                else:
                    arr.popleft()
                n -= 1

    if result:
        print('[', end='')
        if reverse:
            for i in range(n-1, -1, -1):
                print("{}".format(arr[i]), end='')
                if i != 0:
                    print(",", end='')
        else:
            for i in range(n):
                print("{}".format(arr[i]), end='')
                if i != n-1:
                    print(",", end='')
        print(']')
    else:
        print('error')