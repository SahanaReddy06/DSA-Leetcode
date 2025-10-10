class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0              # number of subarrays found
        prefix_sum = 0         # running total (sum from start till now)
        prefix_map = {0: 1}    # store how many times each prefix_sum has occurred

        for num in nums:       # go through each number
            prefix_sum += num  # add current number to total

            if prefix_sum - k in prefix_map:      # check if we have a previous prefix that makes sum = k
                count += prefix_map[prefix_sum - k]

            # update prefix_sum frequency
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

        return count
