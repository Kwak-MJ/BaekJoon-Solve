'''
1. 아이디어
kmp를 이용하면 빠르지 않을까?
-> IOI 만 세는 걸로 풀면 더 빠름!

I가 항상 O보다 1개 더 많음

I로 시작하고 I로 끝나는 패턴임

N 으로는 P 모양 정하고
N=1 -> I=2개, O=1개
N -> I=N+1, O=N
전체 개수는 2N+1

S 에는 테스트 할 문자열 들어옴


2. 시간 복잡도

3. 예외 케이스
아예 포함 안될수도?
중복되는 케이스는?
'''
import sys

input = sys.stdin.readline


def failnaive(p):
    result = [0 for _ in range(len(p))]
    i = 0
    j = 1
    while j < len(p):
        if p[i] == p[j]:
            i += 1
            result[j] = i
            j += 1
        else:
            if i != 0:
                i = result[i - 1]
            else:
                result[j] = 0
                j += 1
    return result


def kmp(t, p):
    count = 0
    posT = 0
    posP = 0
    f = failnaive(p)
    while posT < len(t):
        if t[posT] == p[posP]:
            posT += 1
            posP += 1
            if posP == len(p):
                count += 1
                posP = f[posP - 1]
        else:
            if posP == 0:
                posT += 1
            else:
                posP = f[posP - 1]
    return count


n = int(input())
s_len = int(input())
s = input().rstrip()
pattern = "IO" * n + "I"

result = kmp(s, pattern)
print(result)
