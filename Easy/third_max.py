from typing import List
from math import inf

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m1 = m2 = m3 = -inf
        for num in nums:
            if num in [m1, m2, m3]:
                continue
            if num > m1:
                m3, m2, m1 = m2, m1, num
            elif num > m2:
                m3, m2 = m2, num
            elif num > m3:
                m3 = num
        return m3 if m3 != -inf else m1


# ✅ Driver code (this runs in VS Code)
def main():
    nums = [1, 2]   # test input
    
    sol = Solution()
    result = sol.thirdMax(nums)
    
    print("Third maximum number is:", result)


if __name__ == "__main__":
    main()