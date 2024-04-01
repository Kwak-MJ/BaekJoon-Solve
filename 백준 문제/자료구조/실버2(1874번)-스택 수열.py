from collections import deque
n = int(input())
nums = list(range(n, 0, -1))

stack = []
want = deque()
for _ in range(n):
    want.append(int(input()))
result = []

current = want.popleft()
while nums:
    if not stack or stack[-1] != current:
        stack.append(nums.pop())
        result.append('+')
    else:
        stack.pop()
        result.append('-')
        current = want.popleft()

want.appendleft(current)

while stack:
    if stack[-1] == want[0]:
        stack.pop()
        want.popleft()
        result.append('-')
    else:
        break


if want:
    print('NO')
else:
    for i in result:
        print(i)
