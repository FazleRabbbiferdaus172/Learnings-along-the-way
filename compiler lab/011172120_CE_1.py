def regx(s):
    start_sym = ['^', '*']
    mid_sym = ['@', '#', '$']
    if len(s) < 12 or len(s) > 16:
        # print(1)
        return False
    if not s[0] in start_sym and s[0] != 'c':
        # print(2)
        return False
    if s[0] == 'c' and not s[3] in mid_sym:
        # print(3)
        return False
    if s[0] != 'c' and not s[4] in mid_sym:
        return False

    if s[0] == 'c' and s[:3] != 'cse':
        # print("3a")
        return False
    if s[0] != 'c' and s[1:4] != 'cse':
        #print("3b", s[1:4])
        return False
    if int(s[-6]) < 1 or int(s[-6]) > 6:
        # print(4)
        return False
    try:
        temp = s[-5:-1]
        temp = int(temp)
    except:
        return False
    if int(temp) < 1 or int(temp) > 9999:
        print(5)
        return False
    if ord(s[-1]) < ord('a') or ord(s[-1]) > ord('z'):
        print(6)
        return False
    for i in s:
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):

            return False

    return True


while True:
    choice = int(input("""Press 1 for regX or Press 2 to exit: """))
    if choice == 2:
        break
    else:
        if regx(input("Type a string: ")):
            print("ACCEPTED")
        else:
            print("CAN NOT ACCEPT")
