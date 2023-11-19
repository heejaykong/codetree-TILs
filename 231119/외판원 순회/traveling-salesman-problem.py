# 11:26
import sys
input = sys.stdin.readline
n = int(input())
adj = [list(map(int, input().split())) for i in range(n)]


def solution(adj):
    n = len(adj)
    nodes = [i for i in range(2, n + 1)]
    visited = [False] * (n + 1)
    MAX = sys.maxsize
    ans = MAX

    def calc(arr):
        total = 0
        depart = 1
        for dest in arr:
            total += adj[depart-1][dest-1]
            depart = dest
        dest = 1
        total += adj[depart-1][dest-1]
        return total

    arr = []
    len_nodes = len(nodes)
    def choose(curr_leng):
        nonlocal ans

        if curr_leng == len_nodes:
            cost = calc(arr[:])
            ans = min(ans, cost)
            return

        for i in range(len_nodes):
            if visited[nodes[i]]:
                continue

            arr.append(nodes[i])
            visited[nodes[i]] = True

            choose(curr_leng + 1)
            
            arr.pop()
            visited[nodes[i]] = False


    # 출발하는 1과 도착하는 1을 제외하고 그 사이 순열(중복없음)을 구한다
    # 중복없는 순열은 중복순열(for문사용) 로직에 visited만 얹으면 된다
    # 구해진 순열로 실제 비용을 계산해본다
    # 그리고 최소값과 겨루기
    choose(0)
    return ans


print(solution(adj))