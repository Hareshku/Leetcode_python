from typing import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i
        return -1

s = "leetcode"
obj = Solution()
print(obj.firstUniqChar(s))