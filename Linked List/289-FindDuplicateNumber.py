class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=nums[0]
        fast=nums[0]

        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break

        slow=nums[0]
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        return slow

       #Marked Steps

#InitPointers → slow = nums[0], fast = nums[0]
#DetectCycle → move slow 1x, fast 2x until slow == fast
#ResetSlow → slow = nums[0]
#FindDuplicate → move both 1x until slow == fast
#Return → slow is the duplicate

        
