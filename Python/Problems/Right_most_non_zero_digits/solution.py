#!bin/python3


n_t = int(input())
for i in range(n_t):
    m = int(input())
    arr = list(map(int, input().strip().split(' ')))
    prod = 1
    for i in arr:
        prod *= i
    prod = str(prod)
    a = '0'
    for i in prod[::-1]:
        if i != '0':
            a = i
            break
    if a == '0':
        print(-1)
    else:
        print(int(a))
