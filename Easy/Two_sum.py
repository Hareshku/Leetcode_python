# from typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         m = {}
#         for i, x in enumerate(nums):
#             y = target - x
#             if y in m:
#                 return [m[y], i]
#             m[x] = i
            
# # test the function
# s = Solution()
# # nums = [2,7,11,15]
# # target = 9
# nums = [3,2,4]
# target = 6
# # nums = [3,3]
# # target = 6



# result = s.twoSum(nums, target)

# print(result)


from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, x in enumerate(nums):
            y = target - x # y=7
            if y in m: # false
                return [m[y], i] # [0,1]
            m[x] = i # m={2:0}
            
# test the function
s = Solution()
# nums = [2,7,11,15]
# target = 9
nums = [3,2,4]
target = 6
# nums = [3,3]
# target = 6



result = s.twoSum(nums, target)

print(result)