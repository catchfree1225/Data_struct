import sys
input = sys.stdin.readline

def solve():      
    N = 1 << n
    tr = [0] * N * 2
    for i in range(N):
        tr[i + N] = arr[i]
    for i in range(N - 1, 0, -1):
        tr[i] = tr[i << 1] + tr[i << 1 | 1]
    
    def update_point(i, x):
        i += N
        tr[i] = x
        i >>= 1
        while i:
            tr[i] = tr[i << 1] + tr[i << 1 | 1]
            i >>= 1

    mask = 0
    for q in queries:
        if q[0] == 1:
            x, k = (q[1] - 1) ^ mask, q[2]
            update_point(x, k)
        elif q[0] == 2: # reverse
            k = q[1]
            mask ^= (1 << k) - 1
        elif q[0] == 3: # swap
            k = q[1]
            mask ^= 1 << k
        else:
            l, r = q[1] - 1, q[2] # [l, r)
            ans = 0
            v = 1
            for i in range(n + 1):
                if l & v:
                    tmp = l ^ mask >> i << i
                    ans += tr[(tmp + N) // v]
                    l += v
                if r & v:
                    r -= v
                    tmp = r ^ mask >> i << i
                    ans += tr[(tmp + N) // v]
                if l == r: break
                v <<= 1
            print(ans)
    
for _ in range(1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = [tuple(map(int, input().split())) for _ in range(m)]
    solve()
    