from queue import PriorityQueue


def dijkstra(g, s):
    vis, dis = [0]*len(g), [float('inf')]*(len(g))
    # print(vis)
    pq = PriorityQueue()
    dis[s] = 0
    pq.put((0, s))
    while not pq.empty():
        temp = pq.get()
        # print(temp)
        if vis[temp[1]] == 1:
            continue
        vis[temp[1]] = 1
        for i in g[temp[1]]:
            xx = i[1] + temp[0]*(-1)
            #print(i[1], temp[0], xx)
            if xx < dis[i[0]]:
                dis[i[0]] = xx
                pq.put((-xx, i[0]))
    print(vis)
    print(dis)


n = int(input())
g = dict()
for _ in range(n):
    v, e = map(int, input().split())
    for _ in range(e):
        x = tuple(map(int, input().split()))
        if not v in g:
            g[v] = []
        g[v] += [x]

# print(g)
dijkstra(g, 0)
