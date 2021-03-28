lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
              'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special = ['@', '#', '%', '&']
sign = ['+', '-', '.']


def validate_id_other_half(s):
    if len(s) != 6:
        return 0
    if int(s[2]) > 3:
        return 0
    if int(s[3:]) < 1 and int(s[3:]) > 999:
        return 0
    return 1


def validate_id(s):
    if len(s) != 9:
        return "NOT VALID!!!!!"
    if s[:3] != "011":
        return "NOT VALID!!!!!"
    if not validate_id_other_half(s[3:]):
        return "NOT VALID!!!!!"
    return "VALID"


def validate_email(s):
    global num
    ss = ""
    ind = -1
    for x, i in enumerate(s):
        if i in num:
            ss += i
            ind = x
    if not validate_id_other_half(ss):
        return "NOT VALID!!!!!"
    if s[ind+1:] != '@bscse.uiu.ac.bd' and s[ind+1:] != '@bseee.uiu.ac.bd':
        return "NOT VALID!!!!!"
    return "VALID"


def validate_password(s):
    global lower_case, upper_case, num, special
    if len(s) < 8:
        return "NOT VALID!!!!!"
    if s[-1] != 'P':
        return "NOT VALID!!!!!"
    has_l, has_u, has_special, has_num = 0, 0, 0, 0
    for i in s:
        if i in lower_case:
            has_l = 1
        elif i in upper_case:
            has_u = 1
        elif i in special:
            has_special = 1
        elif i in num:
            has_num = 1
        if has_l and has_u and has_special and has_num:
            break
    else:
        return "NOT VALID!!!!!"
    alls = lower_case + upper_case + special + num
    for i in s:
        if not i in alls:
            return "NOT VALID!!!!!"
    return "VALID"


def validate_number(s):
    global num, sign
    alls = num + sign
    if not s[0] in alls:
        return "NOT VALID!!!!!"
    if s.count('.') > 1 or s.count('+') + s.count('-') > 1:
        return "NOT VALID!!!!!"
    if s[-1] == '.' or s[-1] == '+' or s[-1] == '-':
        return "NOT VALID!!!!!"
    for i in s[1:]:
        if not i in num+['.']:
            print(i)
            return "NOT VALID!!!!!"
    return "VALID"


def validate_string(s):
    global num
    if not "UIU" in s:
        return "NOT VALID!!!!!"
    else:
        ind = s.index('UIU')
    if s[:ind] != s[-1*len(s[:ind]):]:
        return "NOT VALID!!!!!"
    num_count = 0
    for i in s:
        if i in num:
            num_count += 1
        if num_count > 1:
            return "NOT VALID!!!!!"
    else:
        if num_count == 0:
            return "NOT VALID!!!!!"
    return "VALID"


d = {1: validate_id, 2: validate_email, 3: validate_password,
     4: validate_number, 5: validate_string}

while True:
    print("Menu")
    print("Press 1 to Validate ID")
    print("Press 2 to Validate email:")
    print("Press 3 to Validate password")
    print("Press 4 to Validate number")
    print("Press 5 to Validate string")
    print("Press 6 to Exit")
    x = int(input("Put your choice: "))
    if x == 6:
        break
    s = input()
    print(s + " is " + d[x](s))
