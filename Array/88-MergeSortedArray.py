class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1         
        p2 = n - 1          
        p = m + n - 1       
        
        p1 = m - 1  # pointer for last element of nums1's initial part
        p2 = n - 1  # pointer for last element of nums2
        p = m + n - 1  # pointer for last index of nums1 (where we fill elements)

        while p2 >= 0:  # while there are elements in nums2
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

