import matplotlib.pyplot as plt
import math

ranges = [100, 1000, 5000]
for r in ranges:
    z1 = [12, 7]
    z2 = [3, 5]
    z3 = [2, 7]
    u1 = [12/16, 7/16]
    u2 = [3/17, 5/17]
    u3 = [2/15, 7/15]
    u = []
    for i in range(2, r):
        z1.append((13*z1[i-1] + 11*z1[i-2] + 3) % 16)
        z2.append((12*(z2[i-1])**2 + 13*z2[i-2]) % 17)
        z3.append((z3[1-1]**3 + z3[i-2]**2) % 15)
        u1.append(z1[i]/16)
        u2.append(z2[i]/17)
        u3.append(z3[i]/15)

    for i in range(r):
        xx = u1[i]+u2[i]+u3[i]
        xx = math.modf(xx)
        u.append(xx[0])
    print(u)
    plt.bar(range(r), u)
    plt.show()
