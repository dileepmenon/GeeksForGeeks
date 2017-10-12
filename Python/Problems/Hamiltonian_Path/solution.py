#!bin/python3


def is_hamiltonian_path(vert_con, v, l, n, s):
    if len(l) == n:
        return 1
    try:
        for i in vert_con[v]:
            if i not in l:
                s += is_hamiltonian_path(vert_con, i, l+[i], n, 0)
            else:
                pass
        return s
    except:
        return 0


num_T = int(input())
for i in range(num_T):
    n, m = list(map(int, input().strip().split(' ')))
    verts = list(map(int, input().strip().split(' ')))
    vert_con = {}
    for i in range(0, m*2, 2):
        a = min(verts[i], verts[i+1])
        b = max(verts[i], verts[i+1])
        try:
            if b not in vert_con[a]:
                vert_con[a].append(b)
        except:
            vert_con[a] = [b]
        try:
            if a not in vert_con[b]:
                vert_con[b].append(a)
        except:
            vert_con[b] = [a]
    strt = []
    for i, j in vert_con.items():
        if len(j) == 1:
            strt.append(i)
    bool_is_ham = []
    for i in [1] + strt:
        g = is_hamiltonian_path(vert_con, i, [i], n, 0)
        bool_is_ham.append(g >= 1)
    if any(bool_is_ham) is True:
        print(1)
    else:
        print(0)
