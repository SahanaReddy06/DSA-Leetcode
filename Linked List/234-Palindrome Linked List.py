class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        # Step 1: Find middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse second half
        prev = None
        curr = slow   # curr is not head, it is in middle that is y curr=slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Step 3: Compare halves
        first = head
        second = prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True
