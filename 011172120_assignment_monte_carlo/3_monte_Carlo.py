import random
import matplotlib.pyplot as plt
###############Question 3 start###################################
n = [100, 1000, 5000, 10000]
area_m = []
hits = 0
a = 8*4
qqq = [0, 0, 1, 1]
f, axs = plt.subplots(2, 2, figsize=(15, 15))
for i, j in enumerate(n):
    hits = 0
    hit_x, hit_y, miss_x, miss_y = [], [], [], []
    for _ in range(j):
        x = random.uniform(0, 8)
        y = random.uniform(0, 4)
        if x < 4 and y <= (4*x)**0.5:
            hits += 1
            hit_x.append(x)
            hit_y.append(y)
        elif x >= 4 and y <= 8 - x:
            hits += 1
            hit_x.append(x)
            hit_y.append(y)
        else:
            miss_x.append(x)
            miss_y.append(y)
    area_m.append((a*hits)/j)
    axs[qqq[i]][i % 2].scatter(miss_x, miss_y, color="green", label="miss")
    axs[qqq[i]][i % 2].scatter(hit_x, hit_y, color="red", label="hit")
    axs[qqq[i]][i % 2].set_title("Scatter Plot for {} trails".format(j))
    axs[qqq[i]][i % 2].legend(loc="upper right")


print("Area:", *area_m)

plt.show()
#########################Question 3 end ###########################
