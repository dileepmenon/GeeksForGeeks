'''Please note that it's Function problem i.e.
you need to write your solution in the form Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.'''


'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


def countLeaves(root):
    if not root.left and not root.right:
        return 1
    if not root:
        return 0
    return countLeaves(root.left) + countLeaves(root.right)
