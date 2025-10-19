class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy

        # Move fast n+1 steps ahead so slow will point to node before target
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next

        # Remove the nth node
        slow.next = slow.next.next

        return dummy.next




#Create a dummy node at the start (helps handle edge cases like removing the head).
#Move the fast pointer n steps ahead.
#Move both fast and slow until fast reaches the end.
#Now slow.next is the node to remove.
#Update slow.next to skip the node.
#Return dummy.next.
