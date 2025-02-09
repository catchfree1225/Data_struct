def isPalindrome(s: str):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]: return False
        l += 1
        r -= 1
    return True

def count(n: int):
    def dfs(i: int, s: str):
        if i == n:
            cnt = 0
            for i in range(n):
                for j in range(i + 1, n):
                    cnt += isPalindrome(s[i:j+1])
                    if cnt > 1:
                        return 0
            return int(cnt == 1)
        res = 0                
        for c in 'red':
            res += dfs(i + 1, s + c)
        return res
    return dfs(0, '')
        
def solve(x: int):
    if x < 4:
        if x in (0, 1):
            return 0
        elif x == 2:
            return 3
        elif x == 3:
            return 18
    return (x - 4) * 6 + 30

print('測試開始')
for n in range(10):
    cnt1 = count(n)
    cnt2 = solve(n)
    if cnt1 != cnt2:
        print(f'{n}: 出錯了 {cnt1}!={cnt2}')
print('測試結束')
    