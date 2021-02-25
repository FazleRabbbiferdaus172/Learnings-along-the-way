n, m = map(int, input().split())
g = [[] for i in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    g[x] += [y]
    g[y] += [x]
print(g)
r = int(input())
st = [r]
v = [0]*n
par = [0]*n
l = [0]*n


def cyc(form, to):
    global par
    mark = [0]*n
    while form != to:
        mark[form] = 1
        form = par[form]
    mark[to] = 1
    print(mark)


def dfs(g, r, p):
    global v
    global par
    par[r] = p
    v[r] = 1
    if p != None:
        l[r] = l[p] + 1

    # print(r)
    for i in g[r]:
        if v[i] == 1:
            if i != p and l[i] < l[r]:
                cyc(r, i)
            continue
        dfs(g, i, r)


dfs(g, r, None)
