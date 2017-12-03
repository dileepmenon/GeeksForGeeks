'''Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.'''


#function Template for python3
"""
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""
# your task is to complete this function
# function shouldn't return anything
# use self.head to access head in the method
def reverseList(self):
    # Code here
    if self.head is None:
        return None
    p = None
    n = head
    while n:
        t = n
        n = n.next
        t.next = p
        p = t
    self.head = p
