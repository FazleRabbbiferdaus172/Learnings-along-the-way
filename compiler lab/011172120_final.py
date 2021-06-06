with open('in.txt', "r") as inf:
    try:
        x, y = map(int, inf.readline().split())
    except ValueError:
        raise ValueError("Input is not correct")

with open('operators.txt', "r") as inf:
    op = inf.readline().strip()

if not op in ['+', '-', '/', '*']:
    raise Exception("Operator is not correct")

ans = str(x) + op + str(y)
ans = eval(ans)
# print(ans)
with open('out.txt', "w") as ouf:
    ouf.write(str(ans)+'\n')
