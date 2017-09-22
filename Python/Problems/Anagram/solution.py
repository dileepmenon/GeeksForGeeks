#!bin/python3


num_t = int(input())
for i in range(num_t):
    s1 = input().strip()
    s2 = input().strip()
    if sorted(s1) == sorted(s2):
        print('YES')
    else:
        print('NO')
