# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/
#5:18

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Input: s = "leetcode"
        # Output: 0
        
        #Count occurences of digits
        counter = Counter(s)
        #Filter ones that occur once
        counter = {k:v for k,v in counter.items() if v == 1}
        if not len(counter):
            return -1
        #Find indexes
        idx_lst = [s.index(k) for k in counter]
        return min(idx_lst)
        