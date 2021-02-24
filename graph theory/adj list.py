n, m = map(int, input().split())
g = [[] for i in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    g[x] += [y]
    g[y] += [x]


print(g)
