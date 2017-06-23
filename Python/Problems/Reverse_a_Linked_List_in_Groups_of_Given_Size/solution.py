"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
def reverse(head, k):
    grp_ele_coun = 1
    node_grps = []
    grp = []
    while head:
        grp.append(head)
        if grp_ele_coun == k:
            node_grps.append(grp)
            grp = []
            grp_ele_coun = 0
        grp_ele_coun += 1
        head = head.next
    if  grp:
        node_grps.append(grp)
    len_node_grps = len(node_grps)
    if node_grps:
        new_head = node_grps[0][-1]
    for num, k in enumerate(node_grps):
        for i in range(len(k)-1, 0, -1):
            k[i].next = k[i-1]
        if num < len_node_grps-1:
          k[0].next = node_grps[num+1][-1]
        else:
            k[0].next = None
    while new_head:
        print(new_head.data, end=' ')
        new_head = new_head.next
