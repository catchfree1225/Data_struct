import sys
input = sys.stdin.readline

def solve():
    m = {}
    for i in range(k):
        s = sum(a[i])
        for j, x in enumerate(a[i]):
            if s - x in m:
                ai, idx = m[s - x]
                if ai < i:
                    print('YES')
                    print(ai + 1, idx + 1)
                    print(i + 1, j + 1)
                    return
            m[s - x] = i, j
    print('NO')

for _ in range(1):
    k = int(input())
    a = []
    for _ in range(k):
        _ = int(input())
        a.append(list(map(int, input().split())))
    solve()
