#Optimized method-189 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        k = k % n
        
        reverse(0, n-1)         # Step 1: Reverse whole list
        reverse(0, k-1)         # Step 2: Reverse first k elements
        reverse(k, n-1)         # Step 3: Reverse rest


#Left Rotate
def rotate(num, k):
    n=len(num)
    k=k%n                      #it handles k>n
    for _ in range (k):
        temp=num[0]             #store first elemnet 
        for i in range(1, n):
            num[i-1]=num[i]     #put first element at end
        num[n-1]=temp
    return num
num=[1, 2, 3, 4, 5, 6, 7]
k=3
print(rotate(num, k))

or 

def rotate(num, k):
    n=len(num)
    k=k%n
    return num[k:]+num[:k]
num=[1,2,3,4,5,6,7]
k=3
print(rotate(num, k))





#rigth rotate
def rotate(num, k):
    n=len(num)
    k=k%n                      #it handles k>n
    for _ in range (k):
        temp=num[-1]             #store first elemnet 
        for i in range(n-1,0 ,-1):
            num[i]=num[i-1]     #put first element at end
        num[0]=temp
    return num
num=[1, 2, 3, 4, 5, 6, 7]
k=3
print(rotate(num, k))
