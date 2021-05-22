import os
import sys
from types import SimpleNamespace


def InfixToPostfix(s):
    h = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1, '(': -1}
    stk = []
    res = ""
    for i in s:
        if i.isalnum():
            res += i
        elif i == '(':
            stk += ['(']
        elif i == ')':
            while stk and stk[-1] != '(':
                res += stk.pop(-1)
            stk.pop(-1)
        else:
            #print("i", i)
            #print("STK", stk)
            while stk and h[i] <= h[stk[-1]]:
                res += stk.pop(-1)
            stk += [i]

    while stk:
        res += stk.pop(-1)

    return res


def InfixToPrefix(s):
    s = s[::-1]
    s = list(s)
    for i in range(len(s)):
        if s[i] == ')':
            s[i] = '('
        elif s[i] == '(':
            s[i] = ')'
    s = "".join(s)
    res = InfixToPostfix(s)
    return res[::-1]


choice_list = ['console', 'file', 'exit']
choice = ""
while not choice in choice_list:
    choice = input("Enter your choice ({} or {} or {}): ".format(*choice_list))
    choice.lower()

givenString = ""
if choice == choice_list[1]:
    path = input("Enter a valid file path: ")

    while not os.path.exists(path):
        path = input("Enter a valid file path: ")

    with open(path, "r") as inf:
        givenString = inf.readline().strip()
elif choice == choice_list[0]:
    givenString = input("Enter a infix string: ").strip()
else:
    sys.exit(0)

op_choice_list = ["prefix", "postfix"]
op_choice = ""
while not op_choice in op_choice_list:
    op_choice = input("Enter your choice ({} or {}): ".format(*op_choice_list))
    op_choice.lower()


res = ""
if op_choice == op_choice_list[0]:
    res = InfixToPrefix(givenString)
else:
    res = InfixToPostfix(givenString)

if choice == choice_list[1]:
    with open(path, "w") as ouf:
        ouf.writelines([givenString, '\n', res])
else:
    print("Result : ", res)
