s = input()
c = s[0]

for i in range(1, len(s)):
    if s[i] == s[0]:
        c += "$"
    else:
        c += s[i]

print(c)
