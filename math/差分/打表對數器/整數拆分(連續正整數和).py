def count(x: int):
    for st in range(1, x):
        s = st
        for j in range(st + 1, x):
            s += j
            if s > x:
                break
            if s == x:
                return True
    return False
        
def solve(x: int):
    return x & (x - 1) != 0

print('測試開始')
for num in range(500):
    cnt1 = count(num)
    cnt2 = solve(num)
    if cnt1 != cnt2:
        print(f'{num}: 出錯了 {cnt1}!={cnt2}')
print('測試結束')
    