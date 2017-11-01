#!bin/python3


def KP(w_l, p_l, W):
    if not w_l:
        return 0
    if W == 0:
        return 0
    try:
        return d[(p_l[0], len(p_l), W)]
    except:
        if W-w_l[0] >= 0:
            s = max(p_l[0] + KP(w_l[1:], p_l[1:], W-w_l[0]),
                	KP(w_l[1:], p_l[1:], W))
        else:
            s = KP(w_l[1:], p_l[1:], W)
    d[(p_l[0], len(p_l), W)] = s
    return s

num_t = int(input())
for i in range(num_t):
    n = int(input())
    W = int(input())
    p_l = list(map(int, input().strip().split()))
    w_l =  list(map(int, input().strip().split()))
    d = {}
    print(KP(w_l, p_l, W))
