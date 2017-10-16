#!bin/python3
'''Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.'''


# Your task is to complete this function
# Function should return an integer
def minDepth(root):
	if root is None:
		return 0
	if not root.right:
		s = minDepth(root.left)
	elif not root.left:
		s = minDepth(root.right)
	else:
		s = min(minDepth(root.left), minDepth(root.right))
	return 1+s
