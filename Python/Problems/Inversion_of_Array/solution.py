#!bin/python3


def num_inv_pair(arr, n):
    coun = 0
    for i, n_i in enumerate(arr[:-1]):
        for j in range(i+1, n):
            if arr[j] < n_i:
                coun += 1
    return coun


num_t = int(input())
for i in range(num_t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(num_inv_pair(arr, n))
