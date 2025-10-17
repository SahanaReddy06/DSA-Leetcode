class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(start, path):
            res.append(list(path))
    

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])
        return res

#or below one is more optimized

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        def dfs(i):
            if i>=len(nums):
                res.append(list(subset))
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
                
        

        
        

        
