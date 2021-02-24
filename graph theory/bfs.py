n, m = map(int, input().split())
g = [[] for i in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    g[x] += [y]
    g[y] += [x]
print(g)
r = 0
qu = [r]
v = [0]*n
lvl = [0]*n
v[r] = 1
while qu:
    x = qu.pop(0)
    for i in g[x]:
        if not v[i]:
            qu.append(i)
            v[i] = 1
            lvl[i] = lvl[x] + 1

    print(x, "->", end="")
print()
print(lvl)
