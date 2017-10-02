#!bin/python3


def has_sum(arr, n, X):
    p1 = 0
    p2 = n - 1
    while p1 < p2:
        if arr[p1] + arr[p2] == X:
            return 'Yes'
        elif arr[p1] + arr[p2] > X:
            p2 -= 1
        else:
            p1 += 1
    return 'No'


num_t = int(input())
for i in range(num_t):
    n, x = list(map(int, input().strip().split(' ')))
    arr = sorted(list(map(int, input().strip().split(' '))))
    print(has_sum(arr, n, x))
