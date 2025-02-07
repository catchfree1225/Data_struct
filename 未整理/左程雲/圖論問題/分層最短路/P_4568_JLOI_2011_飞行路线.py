import sys
input = sys.stdin.readline
from heapq import heappop, heappush
from math import inf

def solve():
    g = [[] for _ in range(n)]
    for _ in range(m):
        x, y, w = map(int, input().split())
        g[x].append((y, w))
        g[y].append((x, w))
    
    dis = [[inf] * (k + 1) for _ in range(n)]
    dis[s][0] = 0
    q = [(0, s, 0)]
    while q:
        wf, x, kf = heappop(q)
        if wf > dis[x][kf]:
            continue
        if x == t:
            print(wf)
            return
        for y, wt in g[x]:
            if dis[y][kf] > wf + wt:
                dis[y][kf] = wf + wt
                heappush(q, (wf + wt, y, kf))
            if kf < k and dis[y][kf + 1] > wf:
                dis[y][kf + 1] = wf
                heappush(q, (wf, y, kf + 1)) 
    print(-1)
       
for _ in range(1):
    n, m, k = map(int, input().split())
    s, t = map(int, input().split())
    solve()
    