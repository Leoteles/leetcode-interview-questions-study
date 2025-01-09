#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
#3:53
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Input: nums = [2,2,1]
        # Output: 1
        numbers = {}
        for n in nums:
            if n in numbers:
                numbers[n] += 1
            else:
                numbers[n] = 1
        for k,v in numbers.items():
            if v == 1:
                return k
        