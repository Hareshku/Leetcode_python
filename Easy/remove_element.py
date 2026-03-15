from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for x in nums:
            if x != val:
                nums[k] = x
                k += 1
        return k


# -------- main code to run --------
nums = [3,2,2,3]
val = 3

sol = Solution()
result = sol.removeElement(nums, val)

print("k =", result)
print("updated array =", nums[:result])