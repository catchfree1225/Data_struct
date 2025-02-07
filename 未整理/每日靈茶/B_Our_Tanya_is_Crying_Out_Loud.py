from functools import cache
import sys
input = sys.stdin.readline

def solve():
    @cache
    def dfs(i: int) -> int:
        if i < k or k == 1:
            return (i - 1) * A
        return min((i - 1) * A, dfs(i // k) + (i % k) * A + B)
    print(dfs(n))

for _ in range(1):
    n, k, A, B = [int(input()) for _ in range(4)]
    solve()