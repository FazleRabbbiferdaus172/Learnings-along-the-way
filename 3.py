l = [int(x) for x in input("Use a space between numbers: ").split()]
c = 0
ind = list()
for i in l:
    if i % 2 == 0:
        c += 1
        ind.append(i)

print("Count of even number: {}".format(c))
print("Count of odd number: {}".format(len(l)-c))
for i in ind:
    l.remove(i)

print(*l)
