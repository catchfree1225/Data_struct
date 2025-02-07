import sys
input = sys.stdin.readline

def solve():
    ans = []
    not_prime = [True] * 2 + [False] * (n - 1)
    for i in range(2, n + 1):
        if not_prime[i]: continue
        j = i
        while j <= n:
            ans.append(j)
            j *= i
        for j in range(i * i, n + 1, i):
            not_prime[j] = True
    print(len(ans))
    print(*ans)
               
for _ in range(1):
    n = int(input())
    solve()