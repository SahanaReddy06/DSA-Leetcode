class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i=0              # i= the slow pointer points to unique
        for j in range(1, len(nums)):    #j=fast pointer scans through array
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
        return i+1   #gives the count of unique elements.
        
