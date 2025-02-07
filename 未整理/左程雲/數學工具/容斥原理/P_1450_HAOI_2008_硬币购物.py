import sys
input = sys.stdin.readline

def solve():
    MX = int(1e5)
    f = [1] + [0] * MX
    c = [c1, c2, c3, c4]
    for x in c:
        for i in range(x, MX + 1):
            f[i] += f[i - x] # 方案數
            
    for _ in range(n):
        d1, d2, d3, d4, s = map(int, input().split())
        d = [d1, d2, d3, d4]
        illegal = 0
        for stat in range(1, 1 << 4):
            t = s
            sign = -1 # 注意一開始是-1
            for i in range(4):
                if stat >> i & 1:
                    t -= c[i] * (d[i] + 1) # 先用掉超過數量的硬幣
                    sign *= -1
            if t >= 0:
                illegal += f[t] * sign
        print(f[s] - illegal)
    
               
for _ in range(1):
    c1, c2, c3, c4, n = map(int, input().split())
    solve()