import sys
input = sys.stdin.readline


MOD = int(1e9 + 7)
MX = int(1e3)

inv = [1] * 2 + [0] * (MX - 1)
for i in range(2, MX + 1):
    inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD

fac = [1] * 2 + [0] * (MX - 1)
for i in range(1, MX):
    fac[i + 1] = fac[i] * (i + 1) % MOD

inv_fac = [0] * (MX + 1)
inv_fac[MX] = pow(fac[MX], MOD - 2, MOD)
for i in range(MX - 1, -1, -1):
    inv_fac[i] = inv_fac[i + 1] * (i + 1) % MOD

def permute(n, k):
    return fac[n] * inv_fac[n - k] % MOD  
def combine(n, k):
    return permute(n, k) * inv_fac[k] % MOD   

class Solution:
    def numMusicPlaylists(self, n: int, L: int, k: int) -> int:
        def f_music_types(i): # i種音樂可選擇的方法數
            return permute(i, k + 1) * pow(i - k, L - (k + 1), MOD) % MOD

        ans = 0
        sign = 1
        for i in range(n, k, -1): # i >= k+1，(n, 少選數量) * f(n - 少選數量)
            ans = (ans + combine(n, n - i) * f_music_types(i) * sign) % MOD
            sign *= -1
        return ans
    