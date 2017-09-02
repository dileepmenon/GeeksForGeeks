def KP(item_val, item_wt, w_left):
    if w_left <= 0 or not item_val:
        return 0
    elif w_left-item_wt[0] <= 0:
        return KP(item_val[1:], item_wt[1:], w_left)
    else:
        return (max(item_val[0]
                    + KP(item_val[1:], item_wt[1:], w_left-item_wt[0]),
                    KP(item_val[1:], item_wt[1:], w_left)
                   )
               )


num_t = int(input())
for i in range(num_t):
    n = int(input())
    w_max = int(input())
    item_val = list(map(int, input().strip().split(' ')))
    item_wt = list(map(int, input().strip().split(' ')))
    print (KP(item_val, item_wt, w_max))
