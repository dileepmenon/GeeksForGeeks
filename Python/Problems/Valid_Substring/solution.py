#!bin/python3


def get_max_len_valid_substring(s):
    st = [-1]
    result = 0
    for i, n_i in enumerate(s):
        if n_i == '(':
            st.append(i)
        else:
            st.pop()
            if not st:
                st.append(i)
            else:
                curr_len = i - st[-1]
                if result < curr_len:
                    result = curr_len
    return result


num_t = int(input())
for i in range(num_t):
    s = input()
    print(get_max_len_valid_substring(s))
