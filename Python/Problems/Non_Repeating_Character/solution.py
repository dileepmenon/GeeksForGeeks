#!bin/python3


def get_rep_char(s):
    ch = ''
    for i in s:
        if i != ch:
            if s.count(i) == 1 :
                return i
        ch = i
    return -1


num_t = int(input())
for i in range(num_t):
    n = int(input())
    s = input().strip()
    print(get_rep_char(s))
