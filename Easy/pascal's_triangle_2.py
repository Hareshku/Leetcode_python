from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        f = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                f[j] += f[j - 1]
        return f

# case-1
# index=3

# case-2
index=0
obj= Solution()
print(obj.getRow(index))