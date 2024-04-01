# 적절한 답
x, y, side, dia = map(int, input().split())

result1 = (x+y) * side

if (x+y) % 2 == 0:
    result2 = dia * max(x, y)
else:
    result2 = (max(x, y) - 1) * dia + side

result3 = (min(x, y) * dia) + abs(x-y) * side

print(min(result1, result2, result3))


# 내가 작성한 답 (오래걸림)
x, y, side, dia = map(int, input().split())


def solution():
    i = 0
    j = 0
    result = 0
    if 2*side >= dia:
        while True:
            if side > dia:
                if (x-i) == 1 and (y-j) == 0:
                    result += side
                    i += 1
                elif x-i == 0 and y-j == 1:
                    result += side
                    j += 1
                else:
                    result += dia
                    if i > x:
                        i -= 1
                    else:
                        i += 1

                    if j > y:
                        j -= 1
                    else:
                        j += 1
            else:
                if i != x and j != y:
                    result += dia
                    i += 1
                    j += 1
                else:
                    if i == x and j == y:
                        break
                    elif i == x:
                        result += side
                        j += 1
                    elif j == y:
                        result += side
                        i += 1

            if i == x and j == y:
                break
    else:
        result = side * (x+y)

    return result


print(solution())
