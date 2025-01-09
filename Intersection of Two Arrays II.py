#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
#6:50
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Input: nums1 = [1,2,2,1], nums2 = [2,2]
        # Output: [2,2]
        
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        inters_dict = {}
        for num1,v1 in c1.items():
            if num1 in c2:
                inters_dict[num1] = min(v1,c2[num1])
        inters_lst = []
        for num,v in inters_dict.items():
            inters_lst.extend([num]*v)
        return inters_lst