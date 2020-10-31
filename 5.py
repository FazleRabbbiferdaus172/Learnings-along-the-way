l, r = [int(x) for x in input("Use a space between numbers: ").split()]
mark = [0]*(r+1)
prime = []
for i in range(2, r+1):
    if not mark[i]:
        for j in range(i*i, r+1, i):
            mark[j] = 1

for i in range(l, r+1):
    if not mark[i]:
        print(i)
