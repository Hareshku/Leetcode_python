from typing import List, Optional

# Define TreeNode (IMPORTANT)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(nums):
            if not nums:
                return None

            val = max(nums)
            i = nums.index(val)

            root = TreeNode(val)
            root.left = dfs(nums[:i])
            root.right = dfs(nums[i + 1:])

            return root

        return dfs(nums)


# ---- test run ----
sol = Solution()
root = sol.constructMaximumBinaryTree(nums = [3,2,1,6,0,5])
print(root.val)  # should print 6