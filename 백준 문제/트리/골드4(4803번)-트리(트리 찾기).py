# 트리면 True 리턴
def cycle_dfs(current: int):
    visited[current] = True

    for next in tree[current]:
        if parent[current] == next:
            continue

        if visited[next]:
            return True

        parent[next] = current
        visited[next] = True

        if cycle_dfs(next):
            return True

    return False


result = []
while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    tree = [[] for _ in range(n+1)]
    parent = [-1 for _ in range(n+1)]
    visited = [False] * (n+1)
    tree_count = 0

    for _ in range(m):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    # dfs 함수 실행
    for i in range(1, n+1):
        if visited[i] == False:
            parent[i] = i
            if not cycle_dfs(i):
                tree_count += 1

    result.append(tree_count)

# 결과 출력
for i in range(len(result)):
    print('Case {}:'.format(i+1), end=' ')
    if result[i] == 0:
        print('No trees.')
    elif result[i] == 1:
        print('There is one tree.')
    else:
        print('A forest of {} trees.'.format(result[i]))
