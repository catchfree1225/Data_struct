import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

def solve():
    a = []
    for ai, ci in coins:
        ci = min(ci, m // ai)
        i = 1
        while i <= ci:
            a.append(ai * i)
            ci -= i
            i <<= 1
        if ci:
            a.append(ai * ci)
    
    f = [0] * (m + 1)
    f[0] = 1
    for ai in a:
        for i in range(m, ai -1, -1):
            f[i] += f[i - ai]
    print(sum(x > 0 for x in f[1:]))
               
while True:
    n, m = MII()
    if n == m == 0:
        break
    tmp = list(MII())
    coins = [(tmp[i], tmp[i + n]) for i in range(n)]
    solve()