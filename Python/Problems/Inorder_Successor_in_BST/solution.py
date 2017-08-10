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


def getsuccessor(root, X, recent_left_node):
	if X.data == root.data:
		if root.right:
			if not root.right.left:
				return root.right
			else:
				return root
		else:
			if recent_left_node:
				return recent_left_node
			else:
			    return -1
	if X.data > root.data:
		return getsuccessor(root.right, X, recent_left_node)
	if X.data < root.data:
		recent_left_node = root
		return getsuccessor(root.left, X, recent_left_node)


def inorderSuccessor(root, X):
	succ = getsuccessor(root, X, None)
	if succ == -1:
	    return None
	if succ.data == X.data:
	    succ = succ.right
	    while succ:
	        temp = succ
	        succ = succ.left
	    return temp
	else:
	    return succ
