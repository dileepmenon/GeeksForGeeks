#!bin/python3


def max_pair(arr, n, d):
    for i, n_i in enumerate(arr):
        for j in range(i+1, n):
            if n_i/arr[j] == float(arr[j]):
                if arr.count(arr[j]) > 1:
                	return n_i
            else:
                    if (n_i/arr[j]).is_integer():
                        if int(n_i/arr[j]) in d:
                        	return n_i
    return -1


num_t = int(input())
for i in range(num_t):
    n = int(input())
    arr = sorted(list(map(int, input().strip().split())))[::-1]
    d = {}
    for i in arr:
        d[i] = 0
    print(max_pair(arr, n, d))
