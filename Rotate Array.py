from typing import List
#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
#28:13
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Input: nums = [1,2,3,4,5,6,7], k = 3
        #Output: [5,6,7,1,2,3,4]
        old_nums = [i for i in nums]
        N = len(nums)
        #k could be bigger than len of nums
        k = k % N
        for i in range(N):
            nums[i] = old_nums[i - k]
        return nums
    
#New O(n) solution
#Dividing array in two and swapping places
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Input: nums = [1,2,3,4,5,6,7], k = 3
        #Output: [5,6,7,1,2,3,4]
        #if k = 10 (bigger than 7), k should be 3
        N = len(nums)
        k = k % N
        #Point of division
        point = N - k
        
        nums[:] = nums[point:] + nums[:point]
        
