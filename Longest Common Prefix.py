# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/
#8:46

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common = strs[0]
        for w in range(1,len(strs)):
            word = strs[w]
            for i in range(len(common)):
                if i < len(word) and common[i] == word[i]:
                    continue
                else:
                    common = common[:i]
                    break
        return common
            
            