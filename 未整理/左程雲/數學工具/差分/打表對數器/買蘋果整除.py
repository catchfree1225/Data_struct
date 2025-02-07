a, b = 8, 6
def count(apple):
    ans = int(1e18)
    for i in range(apple // a + 1):
        for j in range(apple // b + 1):
            if a * i + b * j == apple:
                ans = min(ans, i + j)
    return ans if ans < int(1e18) else -1

def solve(x: int):
    if x % 2:
        return -1
    if x < 18:
        if x == 0:
            return 0
        elif x in (6, 8):
            return 1
        elif x in (12, 14, 16):
            return 2
        else:
            return -1
    return (x - 18) // 8 + 3

print('測試開始')
for apple in range(200):
    cnt1 = count(apple)
    cnt2 = solve(apple)
    if cnt1 != cnt2:
        print(f'{apple}: 出錯了 {cnt1}!={cnt2}')
print('測試結束')
        