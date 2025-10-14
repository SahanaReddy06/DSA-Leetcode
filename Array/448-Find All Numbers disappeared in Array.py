class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for num in nums:
            index=abs(num)-1
            if nums[index]>0:
                nums[index]=-nums[index]


        missing=[]
        for i in range(n):
            if nums[i] > 0:
                missing.append(i+1)
        return missing
        
