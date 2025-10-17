class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        
        def backtrack(path, used):
            if len(path)==len(nums):
                res.append(path[:]) #make a copy
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i]=True
                    path.append(nums[i])
                    backtrack(path, used)
                    path.pop()       #remove last number
                    used[i]=False    #mark unused
        backtrack([],[False]*len(nums))
        return res


        
