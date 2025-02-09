import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

MOD = int(1e9 + 7)
MX = int(20)

fac = [1] * 2 + [0] * (MX - 1)
for i in range(1, MX):
    fac[i + 1] = fac[i] * (i + 1) % MOD

inv_fac = [0] * (MX + 1)
inv_fac[MX] = pow(fac[MX], MOD - 2, MOD)
for i in range(MX - 1, -1, -1):
    inv_fac[i] = inv_fac[i + 1] * (i + 1) % MOD

# 不要使用到fac[n]
def perm(n, k):
    n %= MOD
    res = 1
    for _ in range(k):
        res = (res * n) % MOD
        n -= 1
    return res

def comb(n, k):
    n %= MOD
    return perm(n, k) * inv_fac[k] % MOD   


def solve():
    if sum(a) < s:
        print(0)
        return
    ans = 0
    k = n - 1 # 重複組合，s顆球分到n箱方法數
    for stat in range(1 << n):
        sign = 1
        rest = s + k
        for i in range(n):
            if stat >> i & 1:
                sign *= -1
                rest -= a[i] + 1
        if rest >= k:
            ans = (ans + sign * comb(rest, k)) % MOD
    print(ans)
          
            
for _ in range(1):
    n, s = MII()
    a = list(MII())
    solve()