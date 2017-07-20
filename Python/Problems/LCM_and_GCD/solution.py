#!bin/python3


num_t = int(input())
for i in range(num_t):
    n1, n2 = list(map(int, input().split()))
    if n1 > n2:
        n2, n1 = n1, n2
    for i in range(n2, n1*n2 + 1, n2):
        if i % n1 == 0:
            lcm = i
            break
    gcd = -1
    for i in range(1, n1+1):
        if n1 % i == 0 and n2 % i == 0:
            if i > gcd:
                gcd = i
    print('%d %d'%(lcm, gcd))
