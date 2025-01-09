# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/
# 12:21


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Input: nums = [0,1,0,3,12,0]
        # Output: [1,3,12,0,0,0]
        N = len(nums)
        for i in range(N-1,-1,-1):
            if nums[i] == 0:
                continue
            else:
                break
        last_non_zero = i
        
        i = 0
        while i <= last_non_zero:
            if nums[i] == 0:
                nums[:] = nums[:i] + nums[i+1:] + [0]
                last_non_zero -= 1
            else:
                i += 1