from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())

def solve():
    f = [0] * (m + 1)
    for _ in range(n):
        v, w, s = MII()
        for mod in range(v):
            q = deque()
            for i in range(mod, m + 1, v):
                while q and f[q[-1]] + (i - q[-1]) // w * v <= f[i]:
                    q.pop()
                q.append(i)
                if q[0] == i - v * (s + 1):
                    q.popleft()
                f[i] = f[q[0]] + (i - q[0]) // w * v
    print(f[m])

for _ in range(1):
    n, m = MII()
    solve()
