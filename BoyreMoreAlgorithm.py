#Boyer-Moore Voting Algorithm-majority element
def majority(nums):
    count=0
    element=None
    for num in nums:
        if count==0:
            element=num
        if num==element:
            count+=1
        else:
            count-=1
    return element
arr=[2,2,1,1,1,2,2]
print(majority(arr))
