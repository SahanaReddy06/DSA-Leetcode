#optimize (hashing+sorting)
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums=sorted(nums)
        index={}
        for i, num in enumerate(sorted_nums):
            if num not in index:
                index[num]=i
        index= [index[num] for num in nums]
        return index

#Brute 

def count(nums):
    n=len(nums)
    result=[]

    for i in range(n):
        count=0 #reset count for each i
        for j in range(n):
            if nums[j] < nums[i]:
                count+=1
        result.append(count)
    return result
            

nums = [8, 1, 2, 2, 3]
print(count(nums))
