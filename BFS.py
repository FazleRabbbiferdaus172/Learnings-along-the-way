def bfs(g, v, root):

    color = ["white"]*v
    parent = [None]*v
    distance = [0]*v

    color[root] = "grey"
    distance[root] = 0

    q = []

    q.append(root)

    while len(q):
        n = q.pop(0)
        for i in g[n]:
            if color[i] == "white":
                color[i] = "grey"
                parent[i] = n
                distance[i] += distance[n]+1
                q.append(i)
        color[n] = "black"

    return parent, distance


def print_path(s_node, e_node, parent):
    if s_node == e_node:
        print(s_node, end="-")
    elif parent[e_node] == None:
        print("No path")
    else:
        print_path(s_node, parent[e_node], parent)
        print(e_node, end="-")
