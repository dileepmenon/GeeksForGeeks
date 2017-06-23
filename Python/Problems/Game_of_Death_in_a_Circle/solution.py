#!bin/python3
from collections import deque


num_t = int(input())
for i in range(num_t):
    n, k = list(map(int, input().split(' ')))
    arr = deque(range(1, n+1))
    t = k - 1
    arr.rotate(-t)
    while len(arr) > 1:
       arr.popleft()
       arr.rotate(-t)
    print(arr[0])
