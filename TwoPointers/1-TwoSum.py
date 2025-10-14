#test cases won't pass , use hashmap for leetcode problem
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


#brute
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i]+nums[j]==target:
                    return i,j



        


        
