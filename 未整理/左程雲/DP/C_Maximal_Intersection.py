import sys
input = sys.stdin.readline

def solve():
    def merge(a, b):
        return max(a[0], b[0]), min(a[1], b[1])
    suf = [(0, 0)] * n + [(0, int(1e9))]
    for i in range(n - 1, -1, -1):
        suf[i] = merge(suf[i + 1], a[i])
    
    ans = 0
    pre = (0, int(1e9))
    for i, p in enumerate(a):
        m = merge(pre, suf[i + 1])
        ans = max(ans, m[1] - m[0])     
        pre = merge(pre, p)
    print(ans)

for _ in range(1):
    n = int(input())
    a = [tuple(map(int, input().split())) for _ in range(n)]
    solve()