from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)

# Create object
sol = Solution()

# Test input
nums = [1, 2, 3, 1]
# nums= [1,0,1,1]
# nums=[1,2,3,1,2,3]

# Call function and print result
print(sol.containsDuplicate(nums))