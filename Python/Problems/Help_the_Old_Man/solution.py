def get_move(n_pl, move, f, t, sp):
    if n_pl == 1:
        c[0] += 1
        if c[0] == move:
            print('%s %s'%(f, t))
            return
    else:
        get_move(n_pl-1, move, f, sp, t)
        get_move(1, move, f, t, sp)
        get_move(n_pl-1, move, sp, t, f)


num_t = int(input())
for i in range(num_t):
	n_pl, move = list(map(int, input().split(' ')))
	c = [0]
	get_move(n_pl, move, '1', '3', '2')
