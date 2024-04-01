'''
1. 아이디어
수빈, 동생 모두 정수 칸에 위치
2x 칸으로 순간이동 or 1칸씩 움직여서 동생 찾기
최소한의 시간으로 찾아라

=> 그리디
=> bfs 라고 함! (찾기 힘들다)

순간이동이든 움직임이든 모두 1초 소요


특이점:
-1 을 하고 2배하면 -2의 효과임
2배하고 -1하면 그저 -1의 효과

순간이동 => 1/2는 없음, 무조건 앞으로 2배만 가능

풀이 계획:
기본적으로 동생과의 거리 차이 계산 (동생 - 수빈)
이것이 음수이면 그냥 -1 씩 가야하므로 (거리 차이) 초 만큼 걸림
이것이 양수이고 (수빈의 위치) 보다 크다면, 수빈을 순간이동
이것이 양수이고 (수빈의 위치) 보다 작다면, + 로 이동하거나 -1과 순간이동의 최소 초 선정

2. 시간 복잡도
수빈, 동생의 위치 좌표 -> 모두 0 ~ 10만
아무리 많이 움직여도 10만 초 이하임

O(NlogN) 에 해결

3. 예외 케이스

'''
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
time = [0] * (10**5 + 1)


def bfs():
    q = deque([n])
    while q:
        cur = q.popleft()
        if cur == k:
            return

        for nx in (cur+1, cur-1, cur*2):
            if 0 <= nx <= 10**5 and time[nx] == 0:
                time[nx] = time[cur] + 1
                q.append(nx)
            if nx == k:
                return


bfs()
print(time[k])
