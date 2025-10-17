class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()           #sort

        def backtrack(start, path, total):
            if total==target:
                result.append(list(path))
                return


            for i in range(start, len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:   # Skip duplicates
                    continue
                if total+candidates[i]>target:     #stop too large
                    break     

                path.append(candidates[i])
                backtrack(i+1, path, total+candidates[i])   #I’ve already used candidates[i] once, don’t 
                path.pop()

        backtrack(0, [], 0)
        return result

#In Combination Sum I, you’re adding money to reach a goal balance.
#In Combination Sum II, you’re spending money until your balance hits zero.


        
        
