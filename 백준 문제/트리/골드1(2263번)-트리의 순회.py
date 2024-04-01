# 2024/01/03 레이팅 골드5 -91 -> 골드1문제 푼 뒤: -78 / 13점
import sys
sys.setrecursionlimit(10**5)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))


def preorder(left_in: int, right_in: int, left_po: int, right_po: int):
    if left_po > right_po or left_in > right_in:
        return

    root = postorder[right_po]

    # 5639번보다 메모리 줄이는 부분
    # inorder의 왼쪽 오른쪽 subtree의 개수는
    # postorder에서도 동일해야한다 -> postorder의 재귀 범위 찾기
    boundary_in = inorder.index(root)
    boundary_po = right_po - (right_in - boundary_in + 1)

    print(root, end=' ')
    preorder(left_in, boundary_in-1, left_po, boundary_po)
    preorder(boundary_in+1, right_in, boundary_po+1, right_po-1)


preorder(0, n-1, 0, n-1)
