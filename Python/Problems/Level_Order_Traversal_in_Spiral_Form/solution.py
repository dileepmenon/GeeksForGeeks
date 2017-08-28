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
# your task is to complete this function
# function should print the level order traversal of the binary tree in spiral order
# Note: You aren't required to print a new line after every test case


def printSpiralLevelOrder(root):
    temp = [root]
    coun = 1
    p = get_child(coun, temp)
    s = temp
    while p:
        s += p
        coun += 1
        p = get_child(coun, p)
    for i in s:
        print(i.data, end=" ")


def get_child(coun, li):
    t = []
    for i in li[::-1]:
        if coun % 2 != 0:
            if i.left:
                t.append(i.left)
            if i.right:
                t.append(i.right)
        else:
            if i.right:
                t.append(i.right)
            if i.left:
                t.append(i.left)
    return t
