from collections import Counter


num_t = int(input())
for i in range(num_t):
    n = int(input())
    arr = input().strip().split(' ')
    arr = Counter(arr)
    s = arr.most_common(2)
    print(s[1][0])
