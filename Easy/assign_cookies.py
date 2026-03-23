from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        j = 0
        for i, x in enumerate(g):
            while j < len(s) and s[j] < g[i]:
                j += 1
            if j >= len(s):
                return i
            j += 1
        return len(g)
      
# case-1
# g = [1,2,3], s = [1,1]
# case-2
g = [1,2]
s = [1,2,3]

obj=Solution()
print(obj.findContentChildren(g,s))