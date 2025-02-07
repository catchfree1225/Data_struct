import sys
input = sys.stdin.readline

def solve():
    p2 = ans = 0 # pow_2, 紀錄之前的調整次數
    for i in range(1, n):
        if a[i] <= a[i - 1]: # 會比倍數少一點點
            p2 += ((a[i - 1] - 1) // a[i]).bit_length()
        else:
            k = (a[i] // a[i - 1]).bit_length() - 1
            p2 = max(p2 - k, 0)
        ans += p2
    print(ans)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    solve()
    