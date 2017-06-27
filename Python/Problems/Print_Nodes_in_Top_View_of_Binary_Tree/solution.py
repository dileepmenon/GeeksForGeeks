#!bin/python2

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

from collections import deque


def topView(root):
	q = deque([(root, 0)])
	l_min =  0
	r_max = 0
	top_nodes = [(root.data, 0)]
	while len(q) > 0:
		tup = q.pop()
		temp = tup[0]
		n_l = tup[1]-1
		n_r = tup[1]+1
		if temp.left:
			q.appendleft((temp.left, n_l))
			if n_l < l_min:
				top_nodes.append((temp.left.data, n_l))
				l_min = n_l
		if temp.right:
			q.appendleft((temp.right, n_r))
			if n_r > r_max:
				top_nodes.append((temp.right.data, n_r))
				r_max = n_r
	srt_top_nodes = sorted(top_nodes, key=lambda x: x[1])
	for i in srt_top_nodes:
		print i[0],
