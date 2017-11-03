#!bin/python3


def get_num_path(i, j, m, n):
    if i == m-1 and j == n-1:
        return 1
    if i > m-1:
        return 0
    if j > n-1:
        return 0
    try:
        return d[(i, j)]
    except:
        s = get_num_path(i+1, j, m, n) + get_num_path(i, j+1, m, n)
        d[(i, j)] = s
        return s


num_t = int(input())
for i in range(num_t):
    m, n = list(map(int, input().strip().split()))
    coun = 0
    d = {}
    get_num_path(0, 0, m, n)
    print(d[(0, 0)])
