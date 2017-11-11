#!bin/python3


def get_max_profit(Pi, Wi, Pi_by_Wi, W_lim):
    arr = []
    for i, j, w in zip(Pi, Wi, Pi_by_Wi):
        arr.append((i, j, w))
    arr = sorted(arr, key=lambda x: x[2], reverse=True)
    Pi = []
    Wi = []
    Pi_by_Wi = []
    for i in arr:
        Pi.append(i[0])
        Wi.append(i[1])
        Pi_by_Wi.append(i[2])
    i = 0
    max_prof = []
    while W_lim != 0 and i < len(Pi):
        if Wi[i] <= W_lim:
            max_prof.append(Pi[i])
            W_lim -= Wi[i]
        else:
            w = float(W_lim)/Wi[i]
            max_prof.append(w*Pi[i])
            W_lim -= w*Wi[i]
        i += 1
    return sum(max_prof)


num_t = int(input())
for i in range(num_t):
    N, W_lim = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))
    Pi = []
    Wi = []
    for i in range(0, 2*N, 2):
        Pi.append(arr[i])
        Wi.append(arr[i+1])
    Pi_by_Wi = [i/j for i, j in zip(Pi, Wi)]
    max_prof = get_max_profit(Pi, Wi, Pi_by_Wi, W_lim)
    print('%0.2f'%max_prof)
