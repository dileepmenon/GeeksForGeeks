'''Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.'''


#User function Template for python3
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


def mirror(root):
    t = root.right
    root.right = root.left
    root.left = t
    if root.right:
        mirror(root.right)
    if root.left:
        mirror(root.left)
