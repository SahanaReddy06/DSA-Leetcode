def sum(arr, target):
    arr.sort()
    n=len(arr)
    left=0
    right=n-1
    while left<right:
        if arr[left]+arr[right]==target:
            return left, right
        elif arr[left]+arr[right]>target:
            right-=1
        else:
            left+=1
    return None
arr=[2,7,11,15]
target=9
print(sum(arr, target))



#optimal

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in seen:
                return [seen[comp], i]
            seen[num] = i
        return None


        
