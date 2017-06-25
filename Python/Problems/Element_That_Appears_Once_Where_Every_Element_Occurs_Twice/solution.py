#!bin/python3


num_t = int(input())
for i in range(num_t):
    n = int(input())
    coun_dict = {}
    arr = list(map(int, input().strip().split(' ')))
    for i in arr:
        if i in coun_dict:
            coun_dict[i] += 1
        else:
            coun_dict[i] = 1
    print(list(filter(lambda x: x[1] == 1, coun_dict.items()))[0][0])
