class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        index={}
        for i, num in enumerate(arr):
            complement=target-num
            if complement in index:
                return (index[complement],i)
            index[num]=i
        
