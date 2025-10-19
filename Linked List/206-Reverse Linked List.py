# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        while (curr!=None):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev


#Initialize two pointers:
#prev = None (will become the new tail)
#curr = head (current node being processed)
#Traverse the list while curr is not None:
#Store the next node: next_node = curr.next
#Reverse the pointer: curr.next = prev
#Move prev to current: prev = curr
#Move curr to next: curr = next_node
#After the loop, prev points to the new head of the reversed list.
#Return prev as the new head
        
