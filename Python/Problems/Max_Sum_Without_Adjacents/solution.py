#!bin/python3


num_t = int(input())
for i in range(num_t):
    n = int(input())
    a = list(map(int, input().strip().split(' ')))
    m1_n = max(a[0], a[1]) if len(a) > 1 else a[0]
    m1_p = a[0]
    s = [a[0], a[1]] if len(a) > 1 else [a[0]]
    for i in range(2, n):
        k = m1_n
        m1_n = max(m1_p+a[i], a[i]+s[i-2])
        m1_p = max(k, m1_p)
        m2 = s[i-2] + a[i]
        s.append(m2)
    print(max(m1_n, m1_p))
