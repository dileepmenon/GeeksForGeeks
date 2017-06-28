#!bin/python3

num_t = int(input())
for i in range(num_t):
    n1, n2, n3 = list(map(int, input().strip().split(' ')))
    arr1 = list(map(int, input().strip().split(' ')))
    arr2 = list(map(int, input().strip().split(' ')))
    arr3 = list(map(int, input().strip().split(' ')))
    srt = sorted([(n1, 0), (n2, 1), (n3, 2)], key=lambda x: x[0])
    idx1, idx2, idx3 = [i[1] for i in srt]
    arr = [arr1, arr2, arr3]
    idx2_beg = 0
    m1 = arr[idx1][0]
    for n_j, j in enumerate(arr[idx2]):
        if j >= m1:
            idx2_beg = n_j
            break
    common_ele_12 = []
    for i in arr[idx1]:
        for j in arr[idx2][idx2_beg:]:
            if i == j:
                common_ele_12.append(i)
    idx3_beg = 0
    if common_ele_12:
        m2 = common_ele_12[0]
        for n_l, l in enumerate(arr[idx3]):
            if l >= m2:
                idx3_beg = n_l
                break
        common_ele_23 = []
        for i in common_ele_12:
            for j in arr[idx3][idx3_beg:]:
                if i == j:
                    common_ele_23.append(i)
        if common_ele_23:
            for k in common_ele_23:
                print (k, end= ' ')
            print('')
        else:
            print(-1)
    else:
        print(-1)
