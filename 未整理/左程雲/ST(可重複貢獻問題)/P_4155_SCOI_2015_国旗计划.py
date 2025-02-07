import sys
input = sys.stdin.readline

def solve():
    a = []
    for i in range(n):
        l, r = map(int, input().split())
        a.append([i, l, r + m * (l > r)])
    a.sort(key=lambda x: x[1])
       
    for i in range(n):
        if a[i][1] > a[i][2]:
            a[i][2] += m
        a.append([a[i][0], a[i][1] + m, a[i][2] + m])

    e = n << 1
    k = m.bit_length() - 1
    st = [[-1] * (k + 1) for _ in range(e)]
    nxt = 0
    for i in range(e):
        while nxt + 1 < e and a[i][2] >= a[nxt + 1][1]:
            nxt += 1
        st[i][0] = nxt
    for p in range(k):
        for i in range(e):
            st[i][p + 1] = st[st[i][p]][p]
    
    ans = [0] * n
    for i in range(n):
        idx, aim = a[i][0], a[i][1] + m
        cur = i
        cnt = 1
        for p in range(k, -1, -1):
            nxt = st[cur][p]
            if nxt != -1 and a[nxt][2] < aim:
                cnt += 1 << p
                cur = nxt
        ans[idx] = cnt + 1
    print(*ans)

for _ in range(1):
    n, m = map(int, input().split())
    solve()
