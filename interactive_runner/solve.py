import sys
input = lambda: sys.stdin.readline().strip()
MII = lambda: map(int, input().split())

def query(i: int, j: int) -> int:
    print('?', i, j, flush=True)
    return int(input())

def solve_one():
    n = int(input())
    xs = list(MII())
    vs = [0] * (n + 1)
    for i, x in enumerate(xs, 1):
        vs[x] = i
    
    if sum(v > 0 for v in vs) < n:
        for i in range(1, n + 1):
            if vs[i] == 0:
                d = query(i, 1 + (i == 1))
                break
        print('! A' if d == 0 else '! B', flush=True)
        return
    
    d1n = query(vs[1], vs[n])
    dn1 = query(vs[n], vs[1])
    print('! B' if d1n == dn1 and d1n >= n - 1 and dn1 >= n - 1 else '! A', flush=True)
    
    
def main():
    t = int(input())
    for _ in range(t):
        solve_one()
        input() # take results from judge
 
if __name__ == "__main__":
    main()