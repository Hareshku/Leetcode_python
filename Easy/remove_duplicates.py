from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for x in nums:
            if k == 0 or x != nums[k - 1]:
                nums[k] = x
                k += 1
        return k


nums = [0,0,1,1,1,2,2,3,3,4]

sol = Solution()
k = sol.removeDuplicates(nums)

print("k =", k)
print("unique elements:", nums[:k])