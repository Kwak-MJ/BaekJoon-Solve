# 파이썬 내장함수로도 당연히 가능
# NlogN 이면 해결 가능
# 출력 과정에서 index() 사용 시 for 문과 더불어 O(N^2)
# 딕셔너리 가능
from collections import defaultdict


def mergeSort(given: list):
    n = len(given)

    if n < 2:
        return given

    mid = n//2

    left = mergeSort(given[:mid])
    right = mergeSort(given[mid:])

    return merge(left, right)


def merge(left: list, right: list):
    nl, nr = len(left), len(right)
    merged = []
    i, j = 0, 0

    while i < nl and j < nr:
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        elif left[i] > right[j]:
            merged.append(right[j])
            j += 1
        else:
            merged.append(left[i])
            merged.append(right[j])
            i += 1
            j += 1

    if i == nl:
        merged = merged + right[j:]

    if j == nr:
        merged = merged + left[i:]

    return merged


n = int(input())
nums = list(map(int, input().split()))

sortedNums = (mergeSort(list(set(nums))))
dic = defaultdict()

for i in range(len(sortedNums)):
    dic[sortedNums[i]] = i

for i in nums:
    print(dic[i], end=' ')
