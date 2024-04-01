# 정답1 - 가독성도 좋고 효율성 좋은 방식
# parameters
r = 31
M = 1234567891

n = int(input())
given = input()
result = 0
for i in range(n):
    char = given[i]
    result += (ord(char)-96) * (r**i)

print(result % M)


# 정답2 - 가장 빠른 방식 (python3)
n = int(input())

print(sum((ord(char)-96) * (31**i)
      for i, char in enumerate(input())) % 1234567891)
