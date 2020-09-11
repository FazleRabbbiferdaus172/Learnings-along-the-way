from BFS import bfs, print_path

t = []
with open("input.txt", "r") as inf:
    v_n, e_v = [int(x) for x in inf.readline().split()]
    g = [[] for i in range(v_n)]
    for i in range(e_v):
        t = [int(x) for x in inf.readline().split()]
        g[t[0]].append(t[1])
        t[0], t[1] = t[1], t[0]
        g[t[0]].append(t[1])

    for i, j in enumerate(g):
        print(i, "--", *j)
    print(g)

p, d = bfs(g, v_n, 0)

print_path(0, 2, p)
print()
print(d)
