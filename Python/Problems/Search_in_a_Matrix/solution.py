#!bin/python3
def find_ele(x, arr, m, n):
    r = 0
    c = n - 1
    while True:
        if r >= m or c < 0:
            break
        if arr[r][c] == x:
            return 1
        elif arr[r][c] < x:
            r += 1
        else:
            c -= 1
    return 0


num_t = int(input())
for i in range(num_t):
    m, n = list(map(int, input().strip().split()))
    a = list(map(int, input().strip().split()))
    arr = []
    for i in range(m):
        arr.append(a[i*n:(i+1)*n])
    x = int(input())
    print(find_ele(x, arr, m, n))
