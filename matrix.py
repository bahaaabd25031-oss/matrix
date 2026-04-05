a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
b = [[10, 11], [20, 21], [30, 31]]
c = []

for i in range(len(a)):
    c.append([])
    for j in range(len(b[0])):
        s = 0
        for k in range(len(a[0])):
            s += a[i][k] * b[k][j]
        c[i].append(s)
print(c)