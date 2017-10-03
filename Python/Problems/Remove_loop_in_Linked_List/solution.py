'''Please note that it's Function problem i.e.
you need to write your solution in the form Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.'''


#Your task is to complete this function
#Function should return 1/0 only
def removeTheLoop(head):
    h = head
    vis_node = [h.data]
    while h:
        if h.next != None and h.next.data in vis_node:
            return 1
        else:
            h = h.next
            if h != None:
                vis_node.append(h.data)
    return 0
