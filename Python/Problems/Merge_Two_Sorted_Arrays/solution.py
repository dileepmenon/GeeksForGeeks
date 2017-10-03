#!bin/python3


def merge_srt_arrays(arr1, arr2, m, n):
    p1 = 0
    p2 = 0
    mrg = []
    while p1 < m and p2 < n:
        if arr1[p1] > arr2[p2]:
            mrg.append(arr1[p1])
            p1 += 1
        elif arr1[p1] < arr2[p2]:
            mrg.append(arr2[p2])
            p2 += 1
        else:
            mrg += [arr1[p1]] * 2
            p1 += 1
            p2 += 1
    if p1 == m and p2 != n:
        mrg += arr2[p2:]
    if p2 == n and p1 != m:
        mrg += arr1[p1:]
    return mrg


num_t = int(input())
for i in range(num_t):
    m, n = list(map(int, input().strip().split(' ')))
    arr1 = list(map(int, input().strip().split(' ')))
    for i in range(m-1):
        if arr1[i+1] > arr1[i]:
            arr1 = arr1[::-1]
            break
    arr2 = list(map(int, input().strip().split(' ')))
    for j in range(n-1):
        if arr2[j+1] > arr2[j]:
            arr2 = arr2[::-1]
            break
    merge_arr = merge_srt_arrays(arr1, arr2, m, n)
    for i in merge_arr:
        print(i, end=' ')
    print()
