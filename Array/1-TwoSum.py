#Bruteforce method
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i]+nums[j]==target:
                    return i,j

#optimize
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i, num in enumerate(nums):
            complement=target-num
            if complement in seen:
                return seen[complement],i
            seen[num]=i



        
