import sys
input = lambda: sys.stdin.readline().strip()
import random

from math import inf
def floyd_warshall(n, edges):
    dist = [[inf] * (n+1) for _ in range(n+1)]
    for i in range(n+1):
        dist[i][i] = 0
    for u, v in edges:
        dist[u][v] = 1
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dist[i][k] != inf and dist[k][j] != inf:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

def generate_testcase(n):
    x = [random.randint(1, n) for _ in range(n)]
    y = [random.choice([yi for yi in range(1, n + 1) if yi != xi]) for xi in x]
    
    # 如果仍有重複配對，重試
    if len(set(zip(x, y))) != n:
        return generate_testcase(n)
    return x, y

def handle_testcase():
    n = random.randint(3, 8)
    x, y = generate_testcase(n)
    is_graph = random.choice([True, False])
    
    if is_graph:
        edges = [(x[i], y[i]) for i in range(n)]
        shortest_paths = floyd_warshall(n, edges)
    
    print(n, flush=True)
    print(*x, flush=True)
    
    while True:
        cmd = input().split()
        if cmd[0] == '!':
            is_correct = (cmd[1] == 'A') == is_graph
            print('AC' if is_correct else 'WA', flush=True)
            return is_correct
        if cmd[0] == '?':
            i, j = map(int, cmd[1:])
            if is_graph:
                dist = shortest_paths[i][j]
                print(0 if dist == inf else dist, flush=True)
            else:
                dist = abs(x[i-1] - x[j-1]) + abs(y[i-1] - y[j-1])
                print(dist, flush=True)

def main():
    print(t := 100, flush=True)
    correct = 0
    for _ in range(t):
        correct += handle_testcase()
    print(f'Correct: {correct} / {t}')

if __name__ == "__main__":
    main()