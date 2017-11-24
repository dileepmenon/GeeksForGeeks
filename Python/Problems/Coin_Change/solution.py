#!bin/python3


def get_num_ways(arr, k):
    if k == 0:
        return 1
    if not arr:
        return 0
    if arr == [k]:
        return 1
    try:
        return d[(arr[0], len(arr), k)]
    except:
        s = get_num_ways([i for i in arr if i <= k-arr[0]], k - arr[0]) \
            + get_num_ways(arr[1:], k)
        d[(arr[0], len(arr), k)] = s
        return s


num_t = int(input())
for i in range(num_t):
    n = int(input())
    arr = sorted(list(map(int, input().strip().split())))
    k = int(input())
    d = {}
    print(get_num_ways(arr, k))
