def i(s):
    global tbl
    if '=' in s:
        l, v = s.split("=")
        t, n = l.split(" ")
    else:
        t, n = s.split(" ")
        v = None
    tbl.append([t, n, v])


def r(x):
    global tbl
    r = None
    for i, j in enumerate(tbl):
        if j[1] == x:
            r = i
            break
    tbl.pop(r)


def u(x, t, v):
    global tbl
    r = None
    #print("{} {} {}".format(x, typ, value))
    for i, j in enumerate(tbl):
        if j[1] == x:
            r = i
            break
    if r != None:
        tbl[r] = [t, x, v]


def d():
    global tbl
    for i in range(len(tbl)):
        print(i+1, *tbl[i])


tbl = []
while True:
    t = int(input())
    if t == 1:
        s = input()
        i(s)
    elif t == 2:
        x = input()
        r(x)
    elif t == 3:
        s = input()
        if '=' in s:
            l, v = s.split("=")
            t, x = l.split(" ")
        else:
            t, n = s.split(" ")
            v = None
        u(x, t, v)
    elif t == 4:
        d()
    else:
        break
