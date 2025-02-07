import sys
input = sys.stdin.readline
from collections import deque
MOD = 80112002

def solve():
    g = [[] for _ in range(n)]
    ind = [0] * n
    for _ in range(m):
        x, y = map(lambda x: int(x) - 1, input().split())
        g[x].append(y)
        ind[y] += 1
      
    lines = [0] * n
    q = deque()
    for i, x in enumerate(ind):
        if x == 0:
            lines[i] = 1
            q.append(i)
            
    ans = 0
    while q:
        x = q.popleft()
        if not g[x]:
            ans = (ans + lines[x]) % MOD
        for y in g[x]:
            lines[y] = (lines[y] + lines[x]) % MOD
            ind[y] -= 1
            if ind[y] == 0:
                q.append(y)
    print(ans)
               
for _ in range(1):
    n, m = map(int, input().split())
    solve()
    