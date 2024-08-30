n = 20
for i in range(n+1):
    if i == 0 or i == 1 or i == 2:
        continue
    for j in range(i):
        if j == 0:
            continue
        for k in range(i):
            if k in range(j):
                continue
            if i % (j + k) == 0 and j != k:
                print(i, ' - ', j, '+', k)
