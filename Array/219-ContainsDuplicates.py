#optimize

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index={}
        for i, num in enumerate(nums):
            if num in index and i-index[num]<=k:
                return True
            index[num]=i
        return False

 #brute
def containsNearbyDuplicate(nums, k):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):  # check every pair
            if nums[i] == nums[j] and abs(i - j) <= k:
                return True
    return False


        
        
