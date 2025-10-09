class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_map = {}
        majority = len(nums) // 2

        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
            if count_map[num] > majority:
                return num


