
def dfs(node, parent):
    global tree
    ans = [0, node]

    for i in tree[node]:
        # print(i)
        temp_node, temp_dis = i[0], i[1]

        if temp_node != parent:
            temp = dfs(temp_node, node)
            temp[0] += temp_dis
            ans = max(ans, temp)

    return ans


tree = [
    [(1, 2), (2, 5)],
    [(3, 3), (4, 4)],
    [(5, 6), (6, 7)],
    [],
    [],
    [],
    [],
]

print(dfs(0, 0))
