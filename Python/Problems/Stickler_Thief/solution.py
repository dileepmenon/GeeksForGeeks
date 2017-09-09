#!bin/python3


def MS(arr_h):
    if len(arr_h) == 1:
        return arr_h[0]
    if not arr_h:
        return 0
    if len(arr_h) <= len(MS_Array):
        return MS_Array[len(arr_h) - 1]
    t = max(arr_h[0] + MS(arr_h[2:]),
            MS(arr_h[1:]))
    MS_Array.append(t)
    return t


num_t = int(input())
for i in range(num_t):
    MS_Array = [0]
    num_h = int(input())
    arr_h = list(map(int, input().split()))
    print(MS(arr_h))
