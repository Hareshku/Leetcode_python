from functools import reduce
from operator import xor
from typing import List

#  for sorted list
# class Solution:
#   def findNum(self, nums: list[int]) -> int:
#     n = len(nums)
#     for i in range(n):
#       if nums[i] != i:
#         return i
# list1 = [0, 1, 2, 3, 4, 5, 6, 8, 9]
# obj=Solution()
# print(obj.findNum(list1))


# optimal solution
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(xor, (i ^ v for i, v in enumerate(nums, 1)))
      
list1 = [3, 0, 1]
obj=Solution()
print(obj.missingNumber(list1))