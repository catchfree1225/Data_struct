import sys
input = sys.stdin.readline

def solve():
    n, m = len(s), len(p)
    d, q = 33, int(1e9 + 7)
    s_hash = [0] * (n + 1)
    p_hash = [0] * (m + 1)
    for i, c in enumerate(s):
        s_hash[i + 1] = (d * s_hash[i] + ord(c)) % q
    for i, c in enumerate(p):
        p_hash[i + 1] = (d * p_hash[i] + ord(c)) % q
    def query(l, r, a): #(l, r)
        return (a[r + 1] - a[l] * pow(d, r - l + 1, q)) % q
    
    def isSame(l1, l2, ln):
        return query(l1, l1 + ln - 1, s_hash) == query(l2, l2 + ln - 1, p_hash)
          
    # s[l1, r1] 與 p[l2,] 不同處是否<=k           
    def check(l1, r1, k):    
        cnt = l2 = 0
        while l1 <= r1 and cnt <= k:
            l, r = 0, r1 - l1 + 2
            while l + 1 < r: # 找相同的最大長度
                mid = (l + r) // 2
                if isSame(l1, l2, mid):
                    l = mid
                else:
                    r = mid   
            if l1 + l <= r1:
                cnt += 1
            l1 += l + 1 # 第一個不同的位置
            l2 += l + 1
        return cnt <= k

    ans = sum(check(i, i + m - 1, 3) for i in range(n - m + 1))
    print(ans)
               
for _ in range(int(input())):
    s = input().strip()
    p = input().strip()
    solve()
    