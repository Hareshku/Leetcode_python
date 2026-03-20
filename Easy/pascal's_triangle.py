from typing import List
from itertools import pairwise  

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        f = [[1]]
        for i in range(numRows - 1):
            g = [1] + [a + b for a, b in pairwise(f[-1])] + [1]
            f.append(g)
        return f

sol = Solution()
numRows = 5

result = sol.generate(numRows)

for row in result:
    print(row)