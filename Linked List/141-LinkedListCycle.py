# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
        

#Initialize two pointers: slow and fast, both pointing to head.
#Traverse the list while fast and fast.next are not None.
#Move slow one step at a time (slow = slow.next).
#Move fast two steps at a time (fast = fast.next.next).
#Check if slow and fast meet:
#If slow == fast, a cycle exists → return True.
#If fast or fast.next becomes None, the list ends → return False.
