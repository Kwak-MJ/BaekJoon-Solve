from collections import defaultdict


def boyer_moore(text: str, pattern: str):
    n = len(text)
    m = len(pattern)

    # 먼저 last appear index를 기록해야함
    last = defaultdict(int)
    for i in range(n):
        last[text[i]] = -1
    for i in range(m):
        last[pattern[i]] = i

    # 단어 비교 시작
    i, j = m-1, m-1
    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        else:
            i = i + m - min(j, last[text[i]] + 1)
            j = m-1

    return -1


print(boyer_moore("abdscasdasdfpriorityohyeahszid", "ohyeah"))
