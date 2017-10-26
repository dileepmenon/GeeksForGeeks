'''Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.'''


# your task is to complete this function
# function sort the stack such that top element is max
# funciton should return nothing
# s is a stack
def sorted(s):
    # Code here
    if len(s) == 1:
        return s
    else:
        n = len(s)
        for i in range(n-1):
            st = 0
            while st < n-i-1:
                if s[st] < s[st+1]:
                    tmp = s[st+1]
                    s[st+1] = s[st]
                    s[st] = tmp
                st += 1
        return s
