#Brutefore 

def mostWater(height):
    left=0
    right=len(height)-1
    max_area=0
    for left in range(len(height)):
        for right in range(left+1, len(height)):
            area= (right-left) * min(height[right], height[left])
            max_area=max(max_area, area)
    return max_area
height=[1,8,6,2,5,4,8,3,7]
print(mostWater(height))


#optimize 

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_area=0
        while left<right:
            area= (right-left) * min(height[right], height[left])
            max_area=max(max_area, area)
        
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area


#formula
#Area=(j−i)×min(height[i],height[j])
#(j - i) → the width (distance between the lines)
#min(height[i], height[j])
