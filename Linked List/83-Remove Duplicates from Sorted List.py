# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        while cur and cur.next:
            if cur.val==cur.next.val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return head


          

#InitPointer → Set current = head
#TraverseList → While current and current.next are not None:
#CheckDuplicate → If current.val == current.next.val:
#Skip the next node: current.next = current.next.next
#Else: #MoveForward → current = current.next
#ReturnHead → Return head
