o = [int(x) for x in input("Use a space between numbers: ").split()]
t = [int(x) for x in input("Use a space between numbers: ").split()]
n = []

for i in range(1, len(o), 2):
    n.append(o[i])
for i in range(0, len(t), 2):
    n.append(t[i])

print(*n)
