# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #i will create a dummy node to ensure that there is a start to ListNode, without being empty
        #this helps elimimate all the edge case from the start
        #i set the curr to dummy which progresses and track the tail
        #i will use a while loop to make sure list1 and list2 is not null (not empty)
        #i will compare list1 to list2
            #if list1 < list2
                #i will point curr to list1 
                #i will set curr = list1 so that curr moves to list1 as its current tail
                #i will set list1 to the next
            #else:
                #i do the same for above, but instead of list1, i do for list2
        #after the while loop runs, I need to make sure that if list1 not empty, i can append everything to the curr node
        #i can also append everything else if list2 not empty 
        #i will update the head of the dummy to the next (the start) to ensure I return the correct head and tail

        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
        if list1:
            curr.next = list1
        elif list2: 
            curr.next = list2
        return dummy.next 