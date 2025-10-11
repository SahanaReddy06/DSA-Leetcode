class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array
        result = []  # To store the final triplets

        -# Step 2: Go through each number in array
        for i in range(len(nums)):
            # Step 3: Skip duplicates for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1  # left pointer
            right = len(nums) - 1  # right pointer

            # Step 4: Use two pointers to find other two numbers
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                   # Step 5: Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1  # Need bigger number
                else:
                    right -= 1  # Need smaller number

        return result
