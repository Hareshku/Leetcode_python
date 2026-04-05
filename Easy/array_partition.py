from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
      
      
array= [1,4,3,2]
obj = Solution()
print(obj.arrayPairSum(array))