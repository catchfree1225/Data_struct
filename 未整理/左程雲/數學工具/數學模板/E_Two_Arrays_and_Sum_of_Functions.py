import sys
input = sys.stdin.readline
MII = lambda: map(int, input().split())
MOD = 998244353

def solve():
    a, b = list(MII()), list(MII())
    for i in range(n): # a不能動，只能算a加權
        a[i] *= (i + 1) * (n - i)
    # 反序和 ≤ 亂序和 ≤ 同序和
    a.sort(reverse=True)
    b.sort()
    print(sum(x * y for x, y in zip(a, b)) % MOD)
               
for _ in range(1):
    n = int(input())
    solve()