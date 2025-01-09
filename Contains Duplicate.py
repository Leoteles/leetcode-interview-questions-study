# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/
#1:13

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True
        