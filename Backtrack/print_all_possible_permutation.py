def backtrack(s, rem):
    global vis, ans
    if rem == 0:
        x = "".join(s)
        ans.append(x)
        return
    for i in range(ord('a'), ord('z')+1):
        if chr(i) in vis and vis[chr(i)] == 1:
            s += [chr(i)]
            vis[chr(i)] = 0
            backtrack(s, rem-1)
            s.pop(-1)
            vis[chr(i)] = 1


s = input()

vis = {}

for i in s:
    vis[i] = 1
ans = []
backtrack([], len(s))
print(*ans, sep='\n')
