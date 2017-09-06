def WordsInDict(s, word_list):
    n = 0
    for i in s:
        temp = i
        if i in word_list:
            n += 1
        else:
            for j in word_list:
                if j in i:
                    i = i.replace(j, '')
            if not i:
                n += 1
                word_list.append(temp)
    return n


n = int(input())
for i in range(n):
    num_word = int(input())
    w = input().strip().split(' ')
    w = sorted(w, key=lambda x: len(x))[::-1]
    s = input().strip().split(' ')
    print(WordsInDict(s, w))
