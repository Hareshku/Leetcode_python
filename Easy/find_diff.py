from typing import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cnt = Counter(s)
        for c in t:
            cnt[c] -= 1
            if cnt[c] < 0:
                return c
         
s1= "abcd"  
s2= "abcde"   
obj= Solution()
print(obj.findTheDifference(s1, s2))