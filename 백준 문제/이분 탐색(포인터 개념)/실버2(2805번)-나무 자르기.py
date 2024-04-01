'''
1. 아이디어
H = 설정 높이
[나무 높이들 - 설정 높이] 의 총합 = 가져가는 나무의 길이

이분 탐색 진행하면 되지 않을까?

입력 {
    N (나무의 수), M (가져가려는 최소 길이)
    나무의 높이 순서대로
}

출력 {
    H
}

2. 시간 복잡도
NlogN 까지 끝내면 가능
정렬 -> NlogN
이분탐색 -> NlogN

내 풀이는 메모리 초과 떴음 -> 설정 길이를 리스트로 만들면 당연히 메모리 터짐

3. 예외
길이 1 이런경우
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort()

left = 0
right = max(trees) - 1

result = 0

while left <= right:
    mid = (left + right) // 2

    cut_sum = 0
    for tree in trees:
        if tree > mid:
            cut_sum += (tree - mid)

    if cut_sum >= m:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)