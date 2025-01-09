# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/
# 5:01

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Input: nums = [2,7,11,15], target = 9
        # Output: [0,1]
        N = len(nums)
        for i in range(N-1):
            for j in range(i+1,N):
                if nums[i]+nums[j] == target:
                    return [i,j]