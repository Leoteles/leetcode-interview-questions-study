# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/
#41:45


#The algorithm for myAtoi(string s) is as follows:
#Whitespace: Ignore any leading whitespace (" ").
#Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
#Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
#Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.

class Solution:
    def myAtoi(self, s: str) -> int:
        #123
        if not len(s):
            return 0
        #Ignoring whitespace
        for i in range(len(s)):
            if s[i] == ' ':
                continue
            else:
                break
        s = s[i:]
        #Sign
        neg = False
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            s = s[1:]
            neg = True
        
        #Conversion
        #ignoring leading zeros
        for i in range(len(s)):
            if s[i] == '0':
                continue
            else:
                break
        s = s[i:]
        #Finding end of digits
        for i in range(len(s)):
            if s[i] in '1234567890':
                continue
            else:
                s = s[:i]
                break
        if not len(s):
            return 0
        
        #Rounding
        if not neg:
            lim = str((2**31)-1)
            rounded = int(lim)
        else:
            lim = str(2**31)
            rounded = -int(lim)
        if len(s) > len(lim):
            return rounded
        elif len(s) == len(lim):
            for i,j in zip(s,lim):
                if i > j:
                    return rounded
                elif i == j:
                    continue
                else:
                    break
        print(s)
        s = int(''.join(s))
        s = s if not neg else -s
        return s
        
            
            