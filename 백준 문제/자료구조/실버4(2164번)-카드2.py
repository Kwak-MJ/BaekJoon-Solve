from collections import deque

n = int(input())
nums = deque(range(1, n+1))

while len(nums) > 1:
    nums.popleft()
    nums.append(nums.popleft())

print(nums[0])
