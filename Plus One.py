# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
#4:32

#Transforming into int, adding one and back to string and to array
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Input: digits = [1,2,3]
        # Output: [1,2,4]
        str_num = ''.join(str(i) for i in digits)
        
        num = int(str_num) + 1
        new_str_num = [int(i) for i in str(num)]
        return new_str_num



#Iterating elements and using carry flag
#16:34
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Input: digits = [1,2,3]
        # Output: [1,2,4]
        N = len(digits)
        #least sig
        if digits[N-1] == 9:
            new_digits = [0]
            carry = True
        else:
            new_digits = [digits[N-1]+1]
            carry = False
            
        for i in range(N-2,-1,-1):
            num = digits[i]
            if carry:
                num += 1
            if num == 10:
                new_digits = [0] + new_digits
                carry = True
            else:
                new_digits = [num] + new_digits
                carry = False
        if carry:
            new_digits = [1] + new_digits
        return new_digits