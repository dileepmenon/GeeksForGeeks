#!bin/python3


def get_max(arr):
    if not arr:
        return 0
    try:
        return d[(arr[0], len(arr))]
    except:
        s =  max(arr[0] + get_max(arr[2:]),
                 get_max(arr[1:]))
        d[(arr[0], len(arr))] = s
        return s


num_t = int(input())
for i in range(num_t):
    n = int(input())
    d = {}
    arr = list(map(int, input().strip().split()))
    print(get_max(arr))
