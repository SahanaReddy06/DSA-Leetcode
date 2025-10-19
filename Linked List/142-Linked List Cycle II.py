# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

            if slow==fast:
                fast=head
                while (fast!=slow):
                    slow=slow.next
                    fast=fast.next
                return slow
        return None


#Initialize two pointers: slow and fast, both pointing to head.
#Traverse the list to detect a cycle:
#While fast and fast.next are not None:
#Move slow one step (slow = slow.next).
#Move fast two steps (fast = fast.next.next).
#If slow == fast, a cycle exists → break the loop.
#If no cycle is detected (fast or fast.next is None), return None.
#Reset slow to the head of the list.
#Traverse the list again to find the cycle start:
#While slow != fast:
#Move both slow and fast one step (slow = slow.next, fast = fast.next).
#When slow == fast, this is the start of the cycle → return slow.
