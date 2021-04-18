def insert():
    global d
    s = input("Variable declaration: ")
    try:
        typ, name_value = s.split(" ")
        if '=' in name_value:
            name, value = name_value.split('=')
            if typ == 'str':
                value = list(value)
                value.pop(0)
                value.pop(-1)
                value = "".join(value)
            elif typ == 'int':
                value = int(value)
            elif typ == 'float':
                value = float(value)
        else:
            name = name_value
            value = None
    except ValueError:
        typ, name, dummy, value = s.split(" ")
        if typ == 'str':
            value = list(value)
            value.pop(0)
            value.pop(-1)
            value = "".join(value)
        elif typ == 'int':
            value = int(value)
        elif typ == 'float':
            value = float(value)
    try:
        sl = max(d.keys()) + 1
    except:
        sl = 1

    d[sl] = [name, typ, value]


def remove():
    global d
    k = -1
    x = input("Variable Name: ")
    for i in d:
        if d[i][0] == x:
            k = i
            break
    else:
        print("key doesn't exists")

    if k != -1:
        for i in range(k, len(d)):
            d[i] = d[i+1]
        d.pop(len(d))


def updated():
    global d
    x = input("Variable Name: ")
    typ = input("Variable Type: ")
    value = input("Variable value: ")
    #print("{} {} {}".format(x, typ, value))
    if typ == 'str':
        value = list(value)
        value.pop(0)
        value.pop(-1)
        value = "".join(value)
    elif typ == 'int':
        value = int(value)
    elif typ == 'float':
        value = float(value)
    for i in d:

        if d[i][0] == x:
            d[i][1] = typ
            d[i][2] = value
            break
    else:
        print("key {} doesn't exists".format(x))


def display():
    global d
    width = 20
    print("{} {} {} {}".format("sl".ljust(width), "Name".ljust(
        width), "Type".ljust(width), "Value".ljust(width)))
    for i in d:
        print("{} {} {} {}".format(str(i).ljust(width), str(d[i][0]).ljust(
            width), str(d[i][1]).ljust(width), str(d[i][2]).ljust(width)))
    print("End")


d = {}

command_d = {'1': insert, '2': remove, '3': updated, '4': display}

while True:
    description = '''Press 1 to insert data
    Press 2 to remove data
    press 3 to update a variable
    press 4 to display
    press 5 to Exit '''
    print(description)
    c = input("Your choice: ")
    if c == '5':
        break
    else:
        try:
            command_d[c]()
        except KeyError:
            print("{} is not a valid command".format(c))
