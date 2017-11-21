#!bin/python3


num_t = int(input())
for i in range(num_t):
    n = list(map(int, input().strip()))
    idx = -1
    coun = 0
    for j in range(len(n)-1):
        if n[j] % 2 == 0:
            coun += 1
            idx2 = j
            if n[j] < n[-1]:
                idx = j
                break
    if idx >= 0:
        t = n[-1]
        n[-1] = n[idx]
        n[idx] = t
    else:
        if coun > 0:
            t = n[-1]
            n[-1] = n[idx2]
            n[idx2] = t
    print(''.join(map(str, n)))
