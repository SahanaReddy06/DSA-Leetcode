# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow

#InitPointers → Set slow = head and fast = head
#TraverseList → While fast and fast.next are not None:
#Move slow one step: slow = slow.next (#slow moves 1x)
#Move fast two steps: fast = fast.next.next (#fast moves 2x)
#MiddleFound → When loop ends, slow points to the middle node
#ReturnMiddle → Return slow        
