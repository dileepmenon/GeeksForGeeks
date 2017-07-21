'''Please note that it's Function problem i.e.
you need to write your solution in the form Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.'''


'''
class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None
        self.key = k
'''
# your task is to complete this function
# function should return kth smallest element from the BST
inord = []


def inorder_trav(root):
    if root.left:
        inorder_trav(root.left)
    inord.append(root)
    if root.right:
        inorder_trav(root.right)


def inorderSuccessor(root, X):
	inorder_trav(root)
	succ = None
	for i in inord:
	    if i.data > X.data:
	        succ = i
	        break
	if succ:
	    return succ
	else:
	    pass
