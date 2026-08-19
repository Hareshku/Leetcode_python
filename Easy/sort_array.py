class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # first way 
        # nums.sort()
        # return nums

        # 2nd way 
        for i in range(n):
            isSwap = False
            for j in range(n-i-1):
                if nums[j]>nums[j+1]:
                    temp = nums[i]
                    nums[i]= nums[j+1]
                    nums[j+1]=temp
                    isSwap = True
            if not isSwap:
                break
        return nums



