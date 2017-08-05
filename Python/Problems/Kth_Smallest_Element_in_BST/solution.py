'''Please note that it's Function problem i.e.  you need to write your solution
in the form Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online
Judge.'''


'''
class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None
        self.key = k
'''


s = []


def k_smallest_element(root, n):
    temp = root
    if temp.left:
    	k_smallest_element(temp.left, n)
    s.append(temp.data)
    if temp.right:
    	k_smallest_element(temp.right, n)
    return s if len(s) < n else s[n-1]
