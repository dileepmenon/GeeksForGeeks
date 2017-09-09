#!bin/python3
def MS(arr_h):
    if len(arr_h) == 1:
        return arr_h[0]
    if not arr_h[2:]:
        return arr_h[0]
    else:
        return max(arr_ h[0] + MS(arr_h[2:]),
                   MS(arr_h[1:]))


num_t = int(input())
for i in range(num_t):
    num_h = int(input().strip())
    arr_h = list(map(int, input().strip().split()))
    print(MS(arr_h))
