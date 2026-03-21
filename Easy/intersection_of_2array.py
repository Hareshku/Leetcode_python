from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
      
# Case-1
# nums1 = [1,2,2,1] 
# nums2 = [2,2]

# Case-2
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
obj= Solution()
print(obj.intersection(nums1, nums2))