import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

def solve():
    start_hour, start_minute = map(int, ts.split(':'))
    end_hour, end_minute = map(int, te.split(':'))
    cap = (end_hour - start_hour) * 60 + (end_minute - start_minute)
    a = []
    for _ in range(n):
        t, c, p = MII()
        if p == 0:
            p = cap // t
        i = 1
        while i <= p:
            a.append((t * i, c * i))
            p -= i
            i <<= 1
        if p:
            a.append((t * p, c * p))
    a.sort()
    
    f = [0] * (cap + 1)
    hi = 0
    for t, c in a:
        hi += t
        for i in range(min(hi, cap), t - 1, -1):
            f[i] = max(f[i], f[i - t] + c)
    print(max(f))
               
for _ in range(1):
    ts, te, n = input().split()
    n = int(n)
    solve()