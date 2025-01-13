# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
# 4:49

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c_s = Counter(s)
        c_t = Counter(t)
        
        for k in c_s:
            if k not in c_t:
                return False
            elif c_s[k] != c_t[k]:
                return False
        
        for k in c_t:
            if k not in c_s:
                return False
            elif c_t[k] != c_s[k]:
                return False
        
        
        return True
        