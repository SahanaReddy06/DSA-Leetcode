class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        next_greater={}

        for num in nums2:
            while stack and num > stack[-1]:
                prev=stack.pop()
                next_greater[prev]=num
            stack.append(num)

        while stack:
            prev=stack.pop()
            next_greater[prev]=-1
        
        result=[next_greater[num] for num in nums1]
        return result


#Initialize an empty stack → to keep track of elements in decreasing order.
# Create a dictionary next_greater → to store each element’s next greater value.
#Iterate through each number num in nums2.
# While stack is not empty and num > top of stack →
 # • Pop the top element (prev).
 # • Set next_greater[prev] = num (current num is the next greater).
# Push the current number num onto the stack.
# After loop, for all remaining elements in stack → assign -1 (no greater element).
# Build result for each number in nums1 using next_greater[num].
# Return the final result list.
