'''Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.'''


# Your function should return an integer denoting the size of the new list
def remove_duplicate(n, arr):
    i = 0
    while i != len(arr)-1:
        if arr[i] == arr[i+1]:
            del(arr[i])
        else:
            i += 1
    return(len(arr))
