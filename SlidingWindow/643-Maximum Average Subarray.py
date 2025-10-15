class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum=sum(nums[:k])                            #Step 1: Find the sum of the first 'k' elements
        max_sum=window_sum

                                                            #Step 2: Slide the window from index k to end
        for i in range(k, len(nums)):                       # Subtract the element that goes out of the window
                                                            # and add the new element that enters the window
            window_sum=window_sum-nums[i-k]
            window_sum=window_sum+nums[i]
            max_sum=max(max_sum, window_sum)

        return max_sum/k
