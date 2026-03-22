from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = -1
        for j, x in enumerate(nums):
            if x:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

# Driver code (this is what runs in VS Code)
def main():
    nums = [0, 1, 0, 3, 12]
    
    sol = Solution()
    sol.moveZeroes(nums)
    
    print(nums)   # Output will be modified list

if __name__ == "__main__":
    main()