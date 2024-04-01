from collections import deque

# 리스트 복사할 때 주의해야함! (하나의 리스트를 가르키고 있을수도..)

height = int(input())
num = 2**(height+1) - 1

edge_weight = deque(map(int, input().split()))

edge_weight.appendleft(0)

edge_weight = list(edge_weight)


# 왼쪽 자식 얻기
def getLeftChild(x, group):
    return group[2*x + 1]


# 오른쪽 자식 얻기
def getRightChild(x, group):
    return group[2*x + 2]


# 형제 얻기
def getSibling(x, group):
    if x == 1:
        return group[x+1]
    elif x % 2 == 0:
        return group[x-1]
    else:
        return group[x+1]


# 아래서부터 올라오면서 최대인 가중치 합 구하기 -> logN
add_edge_weight = edge_weight[:]
for i in range(2**height - 2, -1, -1):
    add_edge_weight[i] = add_edge_weight[i] + max(getLeftChild(i, add_edge_weight),
                                                  getRightChild(i, add_edge_weight))

# 모든 경로 내려가면서 가중치에 맞게 추가 값 부여 -> N/2
for i in range(1, num):
    sibling = getSibling(i, add_edge_weight)
    if add_edge_weight[i] < sibling:
        edge_weight[i] += sibling - add_edge_weight[i]

print(sum(edge_weight))
