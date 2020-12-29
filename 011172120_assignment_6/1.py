
arr = [[0, 1, 0, 0, 0],
       [0, 0, 1, 0, 0],
       [0, 1, 1, 0, 1],
       [0, 1, 0, 0, 1],
       [0, 0, 0, 0, 0]]

print("At time: 0")

for i in arr:
    print(*i)

temp = [[0]*5 for i in range(5)]
for t in range(1, 20+1):
    for i in range(5):
        for j in range(5):
            cnt = 0
            if i > 0 and arr[i - 1][j] == 1:
                cnt += 1
            if j > 0 and arr[i][j - 1] == 1:
                cnt += 1
            if i > 0 and j > 0 and arr[i - 1][j - 1] == 1:
                cnt += 1
            if i < 5 - 1 and arr[i + 1][j] == 1:
                cnt += 1
            if j < 5 - 1 and arr[i][j + 1] == 1:
                cnt += 1
            if i < 5 - 1 and j < 5 - 1 and arr[i + 1][j + 1] == 1:
                cnt += 1
            if i < 5 - 1 and j > 0 and arr[i + 1][j - 1] == 1:
                cnt += 1
            if i > 0 and j < 5 - 1 and arr[i - 1][j + 1] == 1:
                cnt += 1

            if arr[i][j] == 1 and cnt < 2:
                temp[i][j] = 0
            elif arr[i][j] == 1 and (cnt == 2 or cnt == 3):
                temp[i][j] = 1
            elif arr[i][j] == 1 and cnt > 3:
                temp[i][j] = 0
            elif arr[i][j] == 0 and cnt == 3:
                temp[i][j] = 1
    for i in range(5):
        arr[i] = temp[i].copy()

    print("At time {}: ".format(t))
    for i in arr:
        print(*i)
