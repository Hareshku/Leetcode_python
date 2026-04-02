from typing import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnt = Counter(s)
        for c in t:
            cnt[c] -= 1
            if cnt[c] < 0:
                return False
        return True
      
s = "anagram"
t = "nagaram"

obj = Solution()
print(obj.isAnagram(s, t))