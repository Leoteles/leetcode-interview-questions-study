#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
#11:19
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #nums = [0,0,1,1,1,2,2,3,3,4]
        uniquei = 0
        for i in range(1,len(nums)):
            if nums[i] == nums[uniquei]:
                continue
            else:
                uniquei += 1
                nums[uniquei] = nums[i]
        return uniquei + 1