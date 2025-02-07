import sys
input = sys.stdin.readline

def solve():
    d = [[0] * (n + 2) for _ in range(n + 2)]
    for i1, j1, i2, j2 in modifies:
        i1, j1 = i1 + 1, j1 + 1
        i2, j2 = i2 + 2, j2 + 2
        d[i1][j1] += 1
        d[i2][j1] -= 1
        d[i1][j2] -= 1
        d[i2][j2] += 1
    
    s = d
    for i in range(n):
        for j in range(n):
            s[i + 1][j + 1] += s[i + 1][j] + s[i][j + 1] - s[i][j]
    
    for i in range(1, n + 1):
        print(*s[i][1:n+1])

    
for _ in range(1):
    n, m = map(int, input().split())
    modifies = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
    solve()
    