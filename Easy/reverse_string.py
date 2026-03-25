from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]

str= ["h", "e", "l", "l", "o"]
print(str)
obj= Solution()
obj.reverseString(str)
print(str)