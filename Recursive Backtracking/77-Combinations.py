class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def backtrack( start, path):
            if len(path)==k:
                res.append(list(path))
                return

            for i in range(start, n):
                path.append(i)
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])
        return res
