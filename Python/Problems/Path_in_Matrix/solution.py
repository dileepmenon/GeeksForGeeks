#!bin/python3


def getmaxpath(mat, r, c, k, tab, n):
    if k < 0:
        return 0
    if tab[r][c] > 0:
        return tab[r][c]
    else:
        if r+1 >= n:
            a1, a2, a3 = -1, -1, -1
        else:
            if c-1 < 0:
                a1, a2, a3 = -1, mat[r+1][c], mat[r+1][c+1]
            elif c+1 >= n:
                a1, a2, a3 = mat[r+1][c-1], mat[r+1][c], -1
            else:
                a1, a2, a3  = mat[r+1][c-1], mat[r+1][c], mat[r+1][c+1]

        s = max(k + getmaxpath(mat, r+1, c-1, a1, tab, n),
                k + getmaxpath(mat, r+1, c, a2, tab, n),
                k + getmaxpath(mat, r+1, c+1, a3, tab, n))
        tab[r][c] = s
        return s


num_t = int(input())
for i in range(num_t):
    n = int(input())
    l = list(map(int, input().strip().split(' ')))
    mat = [l[i:i+n] for i in range(0, len(l)-n+1, n)]
    path_sum = []
    tab = []
    for i in range(n):
        tab.append([0]*n)
    for i in range(len(mat[0])):
        path_sum.append(getmaxpath(mat, 0, i, mat[0][i], tab, n))
    print(max(path_sum))
