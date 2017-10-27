#!bin/python3


num_t = int(input())
for i in range(num_t):
    n = int(input())
    arr = list(range(n+1))
    st = 2
    while st <= n**(1/2):
        j = st**2
        while j <= n:
            arr[j] = 0
            j += st
        st += 1
    arr = list(filter(lambda x: x != 0, arr[2:]))
    print(*arr)
