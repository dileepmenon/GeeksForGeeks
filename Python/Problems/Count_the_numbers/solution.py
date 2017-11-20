#!bin/python 3


num_t = int(input())
for i in range(num_t):
    n = int(input())
    l = [1, 2, 3, 4, 5]
    coun = 0
    for i in range(1, n+1):
        if i in l:
            coun += 1
        else:
            num_l = len(str(i))
            k = 0
            t = i
            while t != 0:
                if int(t % 10) in l:
                    k += 1
                t = int(t / 10)
            if k == num_l:
                coun += 1
    print(coun)
