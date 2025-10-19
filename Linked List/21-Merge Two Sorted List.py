# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        tail=dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next=list1       #if list1.val is greater it goes to list1
                list1=list1.next      #list1 moves forward
            else:
                tail.next=list2
                list2=list2.next
            tail=tail.next

        if list1:
            tail.next=list1
        else:
            tail.next=list2
        return dummy.next

#dummy → acts as a starting placeholder (so we don’t need to handle the first node separately).
#tail → always points to the last node of the merged list.
#while list1 and list2 → ensures both lists are processed until one becomes None.
#tail.next = list1/list2 → connects the smaller node each time.
#Finally, return dummy.next (actual merged head).

          
