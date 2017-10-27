def is_hamming(x):
	if x == 1:
		return 1
	if x % 2 == 0:
		return is_hamming(x/2)
	if x % 3 == 0:
		return is_hamming(x/3)
	if x % 5 == 0:
		return is_hamming(x/5)
	return 0


num_t = int(input())
for i in range(num_t):
    n = int(input())
    c = 0
    s = 0
    while True:
        if c == n:
            print(s)
            break
        else:
            s += 1
            if is_hamming(s):
                c += 1
