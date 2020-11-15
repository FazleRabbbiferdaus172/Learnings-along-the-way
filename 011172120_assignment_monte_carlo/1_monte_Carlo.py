import math
import random
import matplotlib.pyplot as plt
###############Question 1 start###################################
n = [100,1000,5000,10000]
pi = []
pi2 = []
area_c = []
hits = 0
low,high = -5,5
r = 3
a = 10
qqq = [0,0,1,1]
f, axs = plt.subplots(3,2,figsize=(15,15))
for i,j in enumerate(n):
  hits = 0
  hit_x,hit_y,miss_x,miss_y = [],[],[],[]
  for _ in range(j):
    x = random.uniform(low,high)
    y = random.uniform(low,high)
    if math.sqrt(x**2 + y**2)<=r:
      hits+=1
      hit_x.append(x)
      hit_y.append(y)
    else:
      miss_x.append(x)
      miss_y.append(y)
  pi.append((hits/j)*(a**2/r**2))
  pi2.append((hits*(5**2)*4)/(j*(3**2)))
  area_c.append(((a**2)*hits)/j)
  axs[qqq[i]][i%2].scatter(miss_x,miss_y, color="green", label="miss")
  axs[qqq[i]][i%2].scatter(hit_x,hit_y, color="red", label="hit")
  axs[qqq[i]][i%2].set_title("Scatter Plot for {} trails".format(j))
  axs[qqq[i]][i%2].legend(loc="upper right")

print("Value of pi:",*pi)
#print("Value of pi2:",*pi2)
print("Value of Area of circles:",*area_c)
#plt.show()
n = [str(i) for i in n]
#print(n)


axs[2][0].bar(n, pi)
axs[2][0].set_title("Number of trials vs Pi")
axs[2][1].bar(n, area_c)
axs[2][1].set_title("Number of trial vs Area of circle")
plt.show()
#########################Question 1 end ###########################