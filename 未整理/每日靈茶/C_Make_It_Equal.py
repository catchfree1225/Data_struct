import sys
input = sys.stdin.readline

def solve_(): # from yefei162
    a = sorted(arr, reverse=True)
    if a[0] == a[-1]:
        print(0)
        return
    ans = 1
    i = s = cnt = 0
    while i < n:
        cost = s - cnt * a[i]
        if cost <= k:
            s += a[i]
            cnt += 1
            i += 1
        else:
            # cost = s - cnt * a[i] <= k
            ans += 1
            new_h = (s - k + cnt - 1) // cnt
            s = new_h * cnt
            if new_h <= a[-1]:
                break            
    print(ans)
    
def solve(): # 算h的diff.
    a = sorted(arr, reverse=True)
    if a[0] == a[-1]:
        print(0)
        return
    ans = 1
    i = s = cnt = 0
    while i < n:
        cost = s - cnt * a[i]
        if cost <= k:
            s += a[i]
            cnt += 1
            i += 1
        else:
            ans += 1
            new_h = (s - k + cnt - 1) // cnt
            s = new_h * cnt
            if new_h <= a[-1]:
                break   
            if (new_h - a[i]) * cnt > k:
                dh = k // cnt
                op = (new_h - a[i] - 1) // dh # s不能被扣太多，扣最小單位
                ans += op
                s -= (dh * op) * cnt           
    print(ans) 
               
for _ in range(1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    solve()
    