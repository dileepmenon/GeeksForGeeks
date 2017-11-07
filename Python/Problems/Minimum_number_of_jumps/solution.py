#!bin/python3


def get_max_steps(arr, n, i, l):
    if i + arr[i] >= n-1:
        return 1 + l
    try:
        return d[(i, l)]
    except:
        s = []
        for j in range(i+1, i+arr[i]+1, 1):
            s.append(get_max_steps(arr, n, j, 1+l))
        if not s:
            t = float('inf')
        else:
            t = min(s)
        d[(i, l)] = t
        return t


num_t = int(input())
for i in range(num_t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    d = {}
    min_num_jmp = get_max_steps(arr, n, 0, 0)
    print(min_num_jmp if min_num_jmp != float('inf') else -1)
