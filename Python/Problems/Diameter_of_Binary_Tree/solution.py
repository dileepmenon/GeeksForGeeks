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
def diameter(root):
    return get_dia(root)[1]
    
def get_dia(root):
    if root == None:
        return 0, 0
    else:
        lst_height, lst_dia = get_dia(root.left)
        rst_height, rst_dia = get_dia(root.right)
        dia = lst_height + rst_height + 1
        max_dia = max(lst_dia, rst_dia, dia)
        if lst_height > rst_height:
            return (1+lst_height), max_dia
        else:
            return (1+rst_height), max_dia
