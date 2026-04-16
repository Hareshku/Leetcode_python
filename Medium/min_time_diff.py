from typing import List
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 24 * 60:
            return 0
        mins = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)
        mins.append(mins[0] + 24 * 60) # make it a circle, linking 1st and last slot

        return min(abs(a - b) for a, b in pairwise(mins))
      
      
      
      
timePoints = ["23:59","00:00"]

obj =Solution()
print(obj.findMinDifference(timePoints))