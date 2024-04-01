# 50 30 24 5 28 45 98 52 60
import sys
sys.setrecursionlimit(10**5)

elements = []
while True:
    try:
        elements.append(int(input()))
    except:
        break


def post_order(left: int, right: int):
    if left > right:
        return

    # len(elements) - 1이 아님!  right + 1이 되어야함, sub tree가 기준이 되어야함
    boundary = right + 1
    for i in range(left+1, right+1):
        if elements[i] > elements[left]:
            boundary = i
            break

    post_order(left+1, boundary-1)
    post_order(boundary, right)
    print(elements[left])


post_order(0, len(elements) - 1)
