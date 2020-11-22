import random
import matplotlib.pyplot as plt
import math


def fun1(x):
    return x * math.exp(x)


def fun(x):
    return (x**2)*math.exp(x)*math.log(x)


def solve(n, a, b):
    fx_bar, fx2_bar = 0, 0
    for _ in range(n):
        x = random.uniform(a, b)
        fx_bar += (fun(x))
        fx2_bar += (fun(x))**2
    fx_bar /= n
    fx2_bar /= n
    inte_value = fx_bar*(b-a)
    error = ((b-a)/(n**0.5))*((fx2_bar - fx_bar**2)**0.5)
    return inte_value, error


N = [100, 1000, 5000, 10000]
error_all = []
for i in N:
    inte, error = solve(i, 0, 2)
    error_all.append(error)
    print("Integral value {} and Error is  {} for {} numbers of trials".format(
        inte, error, i))

#print("test", fun(2))
#print("test", fun1(2))
#print("test", math.log(math.exp(1), 2))
#print("test", math.log(2))
#ans = 5.8784255
N = [str(i) for i in N]

plt.bar(N, error_all)
plt.xlabel("trails")
plt.ylabel("Error")
plt.show()
