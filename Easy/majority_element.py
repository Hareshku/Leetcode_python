from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = m = 0
        for x in nums:
            if cnt == 0:
                m, cnt = x, 1
            else:
                cnt += 1 if m == x else -1
        return m

if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    obj = Solution()
    print(obj.majorityElement(nums))