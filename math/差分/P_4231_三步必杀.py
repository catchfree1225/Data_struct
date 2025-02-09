import sys
input = sys.stdin.readline
from itertools import accumulate

def solve(): 
    d = [0] * (n + 2)
    for l, r, s, e in damage: # start, end  
        l, r = l - 1, r - 1
        k = (e - s) // (r - l)
        d[l] += s
        d[l + 1] += k - s
        d[r + 1] -= k + e
        d[r + 2] += e
    ans = list(accumulate(accumulate(d[:n])))
    mx = xor = 0
    for x in ans:
        mx = max(mx, x)
        xor ^= x
    print(xor, mx) 
               
for _ in range(1):
    n, m = map(int, input().split())
    damage = [map(int, input().split()) for _ in range(m)]
    solve()
    