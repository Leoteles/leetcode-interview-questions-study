# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/
#8:01

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Filtering s
        s = s.lower()
        s = [i for i in s if i in 'abcdefghijklmnopqrstuvwxyz0123456789']
        
        l = 0
        r = len(s) - 1
        
        
        while l < r:
            
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
        
        return True