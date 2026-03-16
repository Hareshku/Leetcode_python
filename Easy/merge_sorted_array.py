from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


# Example 1
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

# # Example 2
# nums1 = [1], 
# m = 1, 
# nums2 = [], 
# n = 0


# # Example 3
# nums1 = [0], 
# m = 0, 
# nums2 = [1], 
# n = 1

obj = Solution()
obj.merge(nums1, m, nums2, n)

print(nums1)