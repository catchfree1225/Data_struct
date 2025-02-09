from functools import cache
@cache
def dfs(rest: int, cur: str):
    enemy = 'B' if cur == 'A' else 'A'
    if rest < 5:
        return enemy if rest in (0, 2) else cur
    pick = 1
    while pick <= rest:
        if dfs(rest - pick, enemy) == cur:
            return cur
        pick *= 4
    return enemy
        
def solve(x: int):
    return 'BABAA'[x % 5]

print('測試開始')
for grass in range(700):
    cnt1 = dfs(grass, 'A')
    print(cnt1)
    # cnt2 = solve(grass)
    # if cnt1 != cnt2:
    #     print(f'{grass}: 出錯了 {cnt1}!={cnt2}')
    # else:
    #     print(f'{grass}: 通過')
print('測試結束')
    