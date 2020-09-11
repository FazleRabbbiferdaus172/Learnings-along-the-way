
trav_time = []


def dfs_inti(g, v, u):
    global trav_time
    color = ["white"] * v
    parent = [None] * v
    trav_time = [[-1, -1] for i in range(v)]
    dfs_util(u, g, color, parent)
    return trav_time


time = 0


def dfs_util(u, g, color, parent):
    global time, trav_time
    color[u] = "grey"
    trav_time[u][0] = time
    for v in g[u]:
        if color[v] == "white":
            parent[v] = u
            dfs_util(v, g, color, parent)
    color[u] = "Black"
    trav_time[u][1] = time
    time += 1
