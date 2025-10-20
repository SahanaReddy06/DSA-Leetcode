class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[-1]*n
        stack=[]
        for i in range(2*n):
            curr=nums[i%n]             #i%n - index , nums[i%n] = number

            while stack and nums[stack[-1]] < curr:
                prev_index=stack.pop()
                res[prev_index]=curr

            if i<n:              #push only first pass
                stack.append(i)

        return res



        
