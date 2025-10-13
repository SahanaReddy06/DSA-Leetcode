class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window=set()
        i=0
        for j in range(len(nums)):
            if nums[j] in window:
                return True
            window.add(nums[j])

            if j-i>=k:
                window.remove(nums[i])
                i+=1
        return False


#brute

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
        return False


        
        
