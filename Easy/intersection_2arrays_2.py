from typing import List, Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = Counter(nums1)
        res = []
        for num in nums2:
            if counter[num] > 0:
                res.append(num)
                counter[num] -= 1
        return res
      
# case-1
# nums1 = [1,2,2,1]
# nums2 = [2,2]

# case-2
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
obj= Solution()

print(obj.intersect(nums1, nums2))
