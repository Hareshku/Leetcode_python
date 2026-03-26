class Solution(object):
    def wordPattern(self, pattern, s):
        s = s.split()
        a = zip(pattern, s)
        return len(pattern) == len(s) and len(set(a)) == len(set(pattern)) == len(set(s))


# ---- Driver code ----
if __name__ == "__main__":
    obj = Solution()
    
    pattern = "abba"
    s = "dog cat cat dog"
    
    result = obj.wordPattern(pattern, s)
    print(result)