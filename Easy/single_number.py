class Solution(object):
    def singleNumber(self, nums):
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]

if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]  
    obj = Solution()       
    result = obj.singleNumber(nums)  
    print(result)