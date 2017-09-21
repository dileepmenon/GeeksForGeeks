#!bin/python3


def is_pythagorean_triplet(arr):
    for i, n_i in enumerate(arr):
        for j in range(i, len(arr)-1):
            if n_i + arr[j] in arr[1:]:
                return 'Yes'
    return 'No'


num_t = int(input())
for i in range(num_t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    srt_arr_sqr = sorted(list(map(lambda x: x**2, arr)))
    print(is_pythagorean_triplet(srt_arr_sqr))
