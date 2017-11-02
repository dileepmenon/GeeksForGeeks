#!bin/python3


def merge_sort(arr, l, r):
    if l < r:
        m = (l + (r-1))//2
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)


def merge(arr, l, m, r):
    mrg = []
    i = l
    j = m + 1
    global coun
    k = 0
    while i <= m and j <= r:
        if arr[i] < arr[j]:
            mrg.append(arr[i])
            i += 1
        elif arr[i] > arr[j]:
            k += 1
            mrg.append(arr[j])
            coun += len(arr[i:m+1])
            j += 1
        else:
            mrg += 2*[arr[j]]
            coun += len(list(filter(lambda x: x != arr[j],
                                    arr[i+1:m+1])))
            i += 1
            j += 1
    if i == m+1 and j < r+1:
        mrg += arr[j:r+1][:]
    if i < m+1 and j == r+1:
        mrg += arr[i:m+1][:]
    arr[l:r+1] = mrg[:]


num_t = int(input())
for i in range(num_t):
    n = int(input())
    arr = list(map(int, input().strip().split(' ')))
    coun = 0
    merge_sort(arr, 0, len(arr)-1)
    print(coun)
