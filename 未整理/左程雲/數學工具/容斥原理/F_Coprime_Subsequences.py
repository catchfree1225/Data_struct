import sys
input = sys.stdin.readline
from collections import Counter

def solve():
    MOD = int(1e9 + 7)
    mx = max(a)
    ct = Counter(a)
    f = [0] * (mx + 1)
    for i in range(mx, 0, -1):
        cnt = 0
        for j in range(i, mx + 1, i):
            cnt = (cnt + ct[j]) % MOD
        f[i] = (pow(2, cnt, MOD) - 1) % MOD
        for j in range(i * 2, mx + 1, i):
            f[i] = (f[i] - f[j]) % MOD
    print(f[1])
               
for _ in range(1):
    n = int(input())
    a = list(map(int, input().split()))
    solve()