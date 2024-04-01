from collections import defaultdict

node_num = int(input())
tree = []
dic = defaultdict()

for i in range(node_num):
    parent, left, right = input().split()
    dic[parent] = i
    tree.append([left, right])


# preorder
def preorder(cur: str):
    cur_idx = dic[cur]
    visited[cur_idx] = True
    print(cur, end='')

    left = tree[cur_idx][0]
    right = tree[cur_idx][1]

    if left != '.' and visited[dic[left]] == False:
        preorder(left)

    if right != '.' and visited[dic[right]] == False:
        preorder(right)


# inorder
def inorder(cur: str):
    cur_idx = dic[cur]

    left = tree[cur_idx][0]
    right = tree[cur_idx][1]

    if left != '.' and visited[dic[left]] == False:
        inorder(left)

    print(cur, end='')
    visited[cur_idx] = True

    if right != '.' and visited[dic[right]] == False:
        inorder(right)


# postorder
def postorder(cur: str):
    cur_idx = dic[cur]

    left = tree[cur_idx][0]
    right = tree[cur_idx][1]

    if left != '.' and visited[dic[left]] == False:
        postorder(left)

    if right != '.' and visited[dic[right]] == False:
        postorder(right)

    print(cur, end='')
    visited[cur_idx] = True


visited = [False] * node_num
preorder('A')
print()

visited = [False] * node_num
inorder('A')
print()

visited = [False] * node_num
postorder('A')
