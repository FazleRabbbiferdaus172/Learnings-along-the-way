n = int(input())
s = "*"
for i in range(1, 2*n):
    if i <= n:
        print(s*i)
    else:
        print(s*(2*n - i))
