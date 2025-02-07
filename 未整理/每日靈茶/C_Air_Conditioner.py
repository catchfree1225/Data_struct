import sys
input = sys.stdin.readline

def solve():
    l, r, pre_t = m, m, 0
    a = sorted(arr)
    for ti, li, ri in a:
        l -= ti - pre_t
        r += ti - pre_t
        l, r = max(l, li), min(r, ri)
        if l > r: # 先滿足，判斷比較快
            print('NO')
            return
        pre_t = ti
    print('YES')

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    solve()
    