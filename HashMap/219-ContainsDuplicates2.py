class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index={}
        for i, num in enumerate(nums):
            if num in index and i-index[num]<=k:
                return True
            index[num]=i
        return False


#brute
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
        return False

        
        
