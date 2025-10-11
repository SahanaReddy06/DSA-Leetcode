class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sum=n*(n+1)//2      #sum of n numbers 
        input_sum=0        

        for i in range(0,n):
            input_sum=input_sum+nums[i]      #suming the given input numbers
        return sum-input_sum
            


        
