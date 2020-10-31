import matplotlib.pyplot as plt

mon = [int(x) for x in input("Use a space between numbers: ").split()]
to = [int(x) for x in input("Use a space between numbers: ").split()]
fa = [int(x) for x in input("Use a space between numbers: ").split()]
sh = [int(x) for x in input("Use a space between numbers: ").split()]
mo = [int(x) for x in input("Use a space between numbers: ").split()]
so = [int(x) for x in input("Use a space between numbers: ").split()]

fig, ax = plt.subplots()
ax.plot(mon, to, label='Toothpaste')
ax.plot(mon, fa, label='Facewash')
ax.plot(mon, sh, label='shampoo')
ax.plot(mon, mo, label='Moisturaizer')
ax.plot(mon, so, label='Soap')
ax.set_xlabel('Month no')
ax.set_ylabel('Sales Unit')
ax.legend()
# plt.show()

plt.scatter(mon, mo, c='green')
plt.legend(labels='Moisturizer sales')
plt.show()

sales_m = []

for i in range(len(mon)):
    sales_m.append(to[i]+fa[i]+sh[i]+mo[i]+so[i])

plt.bar(mon, sales_m)
plt.xlabel('Month no')
plt.ylabel('Sales')
plt.title('Bar chart')
plt.show()
