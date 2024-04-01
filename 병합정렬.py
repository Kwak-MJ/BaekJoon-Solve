# 머지 소트
def mergeSort(l: list):
    if len(l) == 1:
        return l

    mid = len(l) // 2

    left = mergeSort(l[:mid])
    right = mergeSort(l[mid:])

    return merge(left, right)


def merge(left, right):
    i, j = 0, 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            result.append(right[j])
            i += 1
            j += 1

    if i < len(left):
        result = result + left[i:]
    elif j < len(right):
        result = result + right[j:]

    return result


print(mergeSort([4, 6, 8, 22, 3, 525, 123,
      1, 33, 25, 2, 44, 6677, 53, 42, 45]))
