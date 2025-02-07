import sys
input = sys.stdin.readline

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def solve():
    k = max(a).bit_length() - 1
    st = [[0] * (k + 1) for _ in range(n)]
    
    for i in range(n):
        st[i][0] = a[i]
    for p in range(k):
        for i in range(n - (1 << p)):
            st[i][p + 1] = gcd(st[i][p], st[i + (1 << p)][p])
    
    for i in range(m):
        l, r = map(lambda x: int(x) - 1, input().split())
        p = (r - l + 1).bit_length() - 1
        res = gcd(st[l][p], st[r - (1 << p) + 1][p])
        print(res)
    
    
for _ in range(1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    solve()
