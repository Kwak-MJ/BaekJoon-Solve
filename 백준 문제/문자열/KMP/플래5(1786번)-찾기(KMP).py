def failNaive(pattern):     # 실패함수 주의해서 짜기
    result = [0 for _ in range(len(pattern))]
    i = 0
    j = 1
    while j < len(pattern):
        if pattern[i] == pattern[j]:
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


def kmp(text, pattern):
    result = []
    posT = 0
    posP = 0
    f = failNaive(pattern)
    while posT < len(text):
        if text[posT] == pattern[posP]:
            posT += 1
            posP += 1
            if posP == len(pattern):
                result.append(posT - posP + 1)
                posP = f[posP - 1]     # 그냥 0으로 보내면 스킵하게 되는 부분 생김
        else:
            if posP == 0:    # 왜 posT로 두면 안될까?
                posT += 1
            else:
                posP = f[posP - 1]

    return result


text = input()
pattern = input()

result = kmp(text, pattern)
print(len(result))
for i in result:
    print(i, end=" ")
