from typing import List  

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}
        for i, v in enumerate(nums):
            if v in mp and i - mp[v] <= k:
                return True
            mp[v] = i
        return False

sol = Solution()
nums = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter k: "))
print(sol.containsNearbyDuplicate(nums, k))