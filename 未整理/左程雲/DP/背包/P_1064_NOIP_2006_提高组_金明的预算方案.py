import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

def solve():
    items = [(0, 0)] * (n + 1)
    king = [False] * (n + 1)
    follows = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        price, importance, q = MII()
        val = price * importance
        items[i] = price, val
        if q == 0:
            king[i] = True
        else:
            follows[q].append(i)
    # 枚舉: 二進制 or 容量，配件物品數少用二進制，主物品用容量
    a = sorted((items[i][0] + sum(items[k][0] for k in follows[i]), items[i], i) for i in range(1, n + 1) if king[i])
    f = [0] * (cap + 1)
    hi = 0
    for p_tot, (pi, vi), i in a:
        hi += p_tot
        for j in range(min(hi, cap), pi - 1, -1):
            f[j] = max(f[j], f[j - pi] + vi)
            m = len(follows[i])
            for stat in range(1 << m):
                j2, v2 = j - pi, vi
                for k in range(m):
                    if stat >> k & 1 == 0: continue
                    pk, vk = items[follows[i][k]]
                    if j2 >= pk:
                        f[j] = max(f[j], f[j2 - pk] + v2 + vk)
                        j2 -= pk
                        v2 += vk
    print(max(f))
               
for _ in range(1):
    cap, n = MII()
    solve()