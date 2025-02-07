import sys
input = sys.stdin.readline

def solve():
    k = max(h).bit_length() - 1
    st1 = [[0] * (k + 1) for _ in range(n)]
    st2 = [[0] * (k + 1) for _ in range(n)]
    
    for i in range(n):
        st1[i][0] = st2[i][0] = h[i]
    for p in range(k):
        for i in range(n - (1 << p)):
            st1[i][p + 1] = min(st1[i][p], st1[i + (1 << p)][p])
            st2[i][p + 1] = max(st2[i][p], st2[i + (1 << p)][p])
    
    for i in range(q):
        l, r = map(lambda x: int(x) - 1, input().split())
        p = (r - l + 1).bit_length() - 1
        mn = min(st1[l][p], st1[r - (1 << p) + 1][p])
        mx = max(st2[l][p], st2[r - (1 << p) + 1][p])
        print(mx - mn)
    
    
for _ in range(1):
    n, q = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    solve()
