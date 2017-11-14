#!bin/python3

num_t = int(input())
for i in range(num_t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    st = []
    c = 0
    for i in arr:
        if i != 0:
            st.append(i)
        else:
            c += 1
    st += [0] * c
    print(*st)
