import random
import matplotlib.pyplot as plt
import math


def fun2(x):
    return 8-x


def fun1(x):
    return (4*x)**0.5


def solve1(n, a, b):
    # random.seed(10)
    fx_bar, fx2_bar = 0, 0
    for _ in range(n):
        x = random.uniform(a, b)
        fx_bar += (fun1(x))
        fx2_bar += (fun1(x))**2
    fx_bar /= n
    fx2_bar /= n
    inte_value = fx_bar*(b-a)
    error = ((b-a)/(n**0.5))*((fx2_bar - fx_bar**2)**0.5)
    return inte_value, error


def solve2(n, a, b):
    # random.seed(10)
    fx_bar, fx2_bar = 0, 0
    for _ in range(n):
        x = random.uniform(a, b)
        fx_bar += (fun2(x))
        fx2_bar += (fun2(x))**2
    fx_bar /= n
    fx2_bar /= n
    inte_value = fx_bar*(b-a)
    error = ((b-a)/(n**0.5))*((fx2_bar - fx_bar**2)**0.5)
    return inte_value, error


N = [100, 1000, 5000, 10000]
error_all = []
for i in N:
    inte1, error1 = solve1(i, 0, 4)
    inte2, error2 = solve2(i, 5, 8)
    inte = inte1 + inte2
    error = error1 * error2
    error_all.append(error)
    print("Integral value {} and Error is  {} for {} numbers of trials".format(
        inte, error, i))


#ans = 14.9282035
N = [str(i) for i in N]

plt.bar(N, error_all)
plt.xlabel("trails")
plt.ylabel("Error")
plt.show()
