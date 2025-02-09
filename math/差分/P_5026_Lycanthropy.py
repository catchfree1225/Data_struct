import sys
input = sys.stdin.readline

MX, OFFSET = int(1e6 + 1), int(3e4 + 1)
def solve(): 
    d = [0] * MX
    def set(l, r, s, e, k):
        d[l + OFFSET] += s
        d[l + 1 + OFFSET] += k - s
        d[r + 1 + OFFSET] -= k + e
        d[r + 2 + OFFSET] += e
    for v, i in jumps:
        set(i - v * 3 + 1, i - v * 2, 1, v, 1)
        set(i - v * 2 + 1, i, v - 1, -v, -1)
        set(i + 1, i + v * 2, -v + 1, v, 1)
        set(i + v * 2 + 1, i + v * 3 - 1, v - 1, 1, -1)
    for i in range(1, OFFSET + m + 1):
        d[i] += d[i - 1]
    for i in range(1, OFFSET + m + 1):
        d[i] += d[i - 1]
    print(' '.join(map(str, d[OFFSET+1:OFFSET+m+1])))
    
for _ in range(1):
    n, m = map(int, input().split())
    jumps = [map(int, input().split()) for _ in range(n)]
    solve()
    