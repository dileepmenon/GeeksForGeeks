num_t = int(input())
for i in range(num_t):
    r = int(input())
    c = 0
    for i in range(1, r):
        for j in range(1, r):
            if i**2 + j**2 == r**2:
                c += 1
    c = 4 + 4*c
    print(c)
