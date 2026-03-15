from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left


# ----- main code -----
nums = [1, 3, 5, 6]
target = 2

sol = Solution()
result = sol.searchInsert(nums, target)

print("Insert position:", result)