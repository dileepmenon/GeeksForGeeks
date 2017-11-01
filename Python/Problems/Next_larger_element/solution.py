#!bin/python3


def get_next_ele(arr):
    st = []
    for i, n_i in enumerate(arr):
        st.append((i, n_i))
        while len(st) >= 2:
            if st[-2][-1] < st[-1][-1]:
                d[st[-2][-2]] = st[-1][-1]
                st.pop(-2)
            else:
                break


num_t = int(input())
for i in range(num_t):
    n = int(input())
    arr = list(map(int, input().strip().split(' ')))
    d = {i : -1 for i in range(len(arr))}
    get_next_ele(arr)
    print(*list(d.values()))
