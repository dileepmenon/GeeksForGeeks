num_t = int(input())
for i in range(num_t):
    s = input()
    st = []
    for i in s:
        if not st:
            st.append(i)
        elif st[-1] == '{' and i == '}':
            st.pop()
        elif st[-1] == '[' and i == ']':
            st.pop()
        elif st[-1] == '(' and i == ')':
            st.pop()
        else:
            st.append(i)
    if not st:
        print('balanced')
    else:
        print('not balanced')
