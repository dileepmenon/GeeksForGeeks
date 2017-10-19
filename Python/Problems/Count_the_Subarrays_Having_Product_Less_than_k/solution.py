#!bin/python3


def get_output(arr, k, l, coun):
    for p in range(len(arr)):
        if arr[p] < k:
            coun += 1
        m = []
        m.append(arr[p])
        for i in range(len(l)):
            if l[i]*arr[p] < k:
                m.append(l[i]*arr[p])
                coun += 1
            else:
                break
        l = m[:]
    return coun


num_t = int(input())
for i in range(num_t):
    n, k = list(map(int, input().strip().split(' ')))
    arr = list(map(int, input().strip().split(' ')))
    print(get_output(arr, k, [], 0))
