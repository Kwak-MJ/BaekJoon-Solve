# 아이디어
# 유클리드 호제법으로 구해야함
# a, b의 최대 공약수는 a % b = r 일 때 b % r = r' 의 과정을 0까지 반복
# a, b의 최소 공배수는 a * b / (최대 공약수)

a, b = map(int, input().split())


def gcd(a: int, b: int):
    while b > 0:  # 0이 되면 스탑
        a, b = b, a % b
    return a


def lcm(a: int, b: int):
    return int(a*b / gcd(a, b))


print(gcd(a, b))
print(lcm(a, b))
