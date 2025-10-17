class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()           #sort

        def backtrack(start, path, target):
            if target==0:
                result.append(list(path))
                return


            for i in range(start, len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:   # Skip duplicates
                    continue
                if candidates[i]>target:     #stop too large
                    break     

                path.append(candidates[i])
                backtrack(i+1, path, target-candidates[i])   #I’ve already used candidates[i] once, don’t use it again.that why i+1
                path.pop()

        backtrack(0,[], target)
        return result

#In Combination Sum I, you’re adding money to reach a goal balance.

#In Combination Sum II, you’re spending money until your balance hits zero.


        
        
