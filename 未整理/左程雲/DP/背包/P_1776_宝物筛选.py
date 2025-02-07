from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

def solve():
    f = [0] * (m + 1)
    for _ in range(n):
        v, w, s = MII()
        for i in range(w):
            q = deque()
            for j in range((m - i) // w + 1):
                idx = j * w + i
                val = f[idx] - j * v  
                while q and q[-1][1] <= val:
                    q.pop()
                q.append((j, val))
                if j - q[0][0] > s: # j:當前要拿的數量，q[0][0]:前狀態數量
                    q.popleft()     
                f[idx] = q[0][1] + j * v
    print(f[m])
               
for _ in range(1):
    n, m = MII()
    solve()