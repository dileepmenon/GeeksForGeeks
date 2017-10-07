#!bin/python3


def mergeSort(arr, l, r):
    if l < r:
        m = (l+(r-1)) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


def merge(arr, l, m, r):
    i = l
    j = m + 1
    mrg_arr = []
    while i <= m and j <= r:
        if arr[i] < arr[j]:
            mrg_arr.append(arr[i])
            i += 1
        elif arr[i] > arr[j]:
            mrg_arr.append(arr[j])
            j += 1
        else:
            mrg_arr += 2*[arr[i]]
            i += 1
            j += 1
    if i < m+1 and j == r+1:
        mrg_arr += arr[i:m+1]
    if i == m+1 and j < r+1:
        mrg_arr += arr[j:r+1]
    arr[l: r+1] = mrg_arr[:]


arr = list(map(int, input().strip().split(' ')))
n = len(arr)
print ("Given array is")
for i in range(n):
    print ("%d" % arr[i], end=' ')
mergeSort(arr, 0, n-1)
print ("\n\nSorted array is")
for i in range(n):
    print ("%d" % arr[i], end=' ')
