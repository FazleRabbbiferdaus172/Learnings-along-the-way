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

while st:
    x = st.pop(-1)
    if not v[x]:
        print(x, end=" ")
        v[x] = 1
    for i in g[x]:
        if not v[i]:
            st = [i] + st
print()
