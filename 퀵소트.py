def quickSort(arr):
    if len(arr) <= 1:
        return arr
    left, right = 0, len(arr) - 1
    pivot = int((left+right) / 2)
    left_group, equal_group, right_group = [], [], []
    for num in arr:
        if num < arr[pivot]:
            left_group.append(num)
        elif num > arr[pivot]:
            right_group.append(num)
        else:
            equal_group.append(num)
    return quickSort(left_group) + equal_group + quickSort(right_group)
