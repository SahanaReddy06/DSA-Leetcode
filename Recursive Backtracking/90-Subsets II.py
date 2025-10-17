class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()  #sort

        def backtrack(start, path):
            res.append(list(path))
            
            for i in range(start, len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue  #skip
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])
        return res
        
