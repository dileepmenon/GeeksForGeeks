#!bin/python3

num_t = int(input())
all_brac = ['{}' , '()', '[]']
for i in range(num_t):
    num_brac = {'{':0, '}':0, '(':0, ')':0, '[':0, ']':0}
    s = input()
    for j in s:
        num_brac[j] += 1
    bool_t = [True if num_brac[m[0]] == num_brac[m[1]] else False
              for m in all_brac]
    if all(bool_t):
        print('balanced')
    else:
        print('not balanced')
