nums=[3,4,5,1,2]
def check(nums):
    count=0
    n=len(nums)
    for i in range(n):
        if nums[i]>nums[(i+1) % n]:
            count+=1
    return count<=1
print(check([3,4,5,1,2]))
