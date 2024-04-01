n, k = map(int, input().split())


def f(a: int):
    result = 1
    for i in range(2, a+1):
        result *= i
    return result


print(int(f(n) / (f(n-k) * f(k))))
