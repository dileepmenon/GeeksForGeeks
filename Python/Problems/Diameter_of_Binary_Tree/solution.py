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
# Naive Method, Not Optimized


def get_leaves_and_ancestors(root, s, a):
    if not root.left and not root.right:
        a.append(s)
        return 1
    if not root:
        return 0
    if not root.left:
        return get_leaves_and_ancestors(root.right,
                                        s+[root.right.data],
                                        a)
    if not root.right:
        return get_leaves_and_ancestors(root.left,
                                        s+[root.left.data],
                                        a)
    return get_leaves_and_ancestors(root.left, s+[root.left.data], a)\
           + get_leaves_and_ancestors(root.right, s+[root.right.data], a)


def get_dia(r1, r2):
    p = r1[-2::-1]
    q = r2[-2::-1]
    for n1, i in enumerate(p):
        for n2, j in enumerate(q):
            if i == j:
                d1 = n1 + 1
                d2 = n2 + 1
                return d1+d2+1


def diameter(root):
    if not root:
        return 0
    # list of all leaves and its ancestors
    a = []
    get_leaves_and_ancestors(root, [root.data], a)
    dia = []
    for i, a_i in enumerate(a):
        for j in range(i+1, len(a), 1):
            dia.append(get_dia(a[i], a[j]))
    return max(dia)
