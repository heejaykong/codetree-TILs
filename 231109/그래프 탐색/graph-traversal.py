n,m = tuple(map(int, input().split()))
edges = []
for i in range(m):
    x, y = tuple(map(int, input().split()))
    edges.append((x, y))

def solution(n, edges):
    ans = 0

    # 인접리스트 및 visited 만들기
    adj = [list() for i in range(n + 1)]
    visited = [False] * (n + 1)
    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)

    def dfs(start):
        nonlocal ans

        for next_node in adj[start]:
            if visited[next_node]:
                continue
            ans += 1
            visited[next_node] = True
            dfs(next_node)


    # 나와 인접한 노드 개수 세기
    me = 1
    visited[me] = True
    dfs(me)

    return ans


print(solution(n, edges))