import sys
input = sys.stdin.readline

def solve():
    p = sorted(zip(clr, a))
    for i, (c, x) in enumerate(p):
        if (x < i + 1 and c == 'B') or (x > i + 1 and c == 'R'):
            print('NO')
            return
    print('YES')

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    clr = input()
    solve()
    