#!bin/python3


def get_sum(arr, n, i, j):
    if i == n-1:
        return 0
    try:
        return d[(i, j)]
    except:
        s = max(arr[i+1][j-1] + get_sum(arr, n, i+1, j-1) if j-1 >= 0 else 0,
                arr[i+1][j] + get_sum(arr, n, i+1, j),
                arr[i+1][j+1] + get_sum(arr, n, i+1, j+1) if j+1 < n else 0
                )
        d[(i, j)] = s
        return s


num_t = int(input())
for i in range(num_t):
    n = int(input())
    m = list(map(int, input().strip().split()))
    arr = []
    for i in range(0, len(m), n):
        arr.append(m[i:i+n])
    max_l_path = []
    d = {}
    for i in range(n):
        max_l_path.append(arr[0][i] + get_sum(arr, n, 0, i))
    print(max(max_l_path))
