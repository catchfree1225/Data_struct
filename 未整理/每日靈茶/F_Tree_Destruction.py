import sys
input = sys.stdin.readline

def solve():
    g = [[] for _ in range(n)]
    for x, y in edges:
        g[x].append(y)
        g[y].append(x)
    
    def bfs(rt):
        d = [-1] * n
        d[rt] = 0
        q = [rt]
        for x in q:
            for y in g[x]:
                if d[y] == -1:
                    d[y] = d[x] + 1
                    q.append(y)
        return d
    
    d0 = bfs(0)
    fr = d0.index(max(d0))
    d1 = bfs(fr)
    to = d1.index(max(d1))
    d2 = bfs(to)
    deg = [len(g[i]) for i in range(n)] # 無向圖
    q = [i for i in range(n) if deg[i] == 1 and i not in (fr, to)]
    
    ops = []
    ans = 0
    for x in q:
        if d1[x] >= d2[x]:
            ops.append((x, fr, x))
            ans += d1[x]
        else:
            ops.append((x, to, x))
            ans += d2[x]
        for y in g[x]:
            if deg[y] == 0: continue
            deg[y] -= 1
            if deg[y] == 1:
                q.append(y)
    while fr != to:
        ops.append((fr, to, to))
        ans += d1[to]
        for y in g[to]:
            if d1[y] < d1[to]:
                to = y
                break
    print(ans)
    for op in ops:
        print(*[x + 1 for x in op])

for _ in range(1):
    n = int(input())
    edges = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(n - 1)]
    solve()
    