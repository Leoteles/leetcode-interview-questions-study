# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/
#4:37
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Input: s = ["h","e","l","l","o"]
        # Output: ["o","l","l","e","h"]
        j = len(s) -1
        for i in range(len(s)):
            if i >= j:
                break
            aux = s[i]
            s[i] = s[j]
            s[j] = aux
            j -= 1