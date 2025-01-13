# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/
#15:40

#using 64 bit integers
class Solution:
    def reverse(self, x: int) -> int:
        # Input: x = 123; 1
        # Output: 321; -1
        str_x = str(x)
        N = len(str_x)
        str_x = [str_x[i] for i in range(N-1,-1,-1)]
        if x < 0:
            str_x = ['-']+str_x[:-1]
        new_x = int(''.join(str_x))
        if new_x < -(2**31) or new_x > (2**31 - 1):
            return 0
        else:
            return new_x

#11:17
#not using 64 bit integers
class Solution:
    def reverse(self, x: int) -> int:
        # Input: x = 123; 1
        # Output: 321; -1
        str_x = str(x)
        
        if x < 0:
            str_x = str_x[1:]
            neg = True
        else:
            neg = False
            
        N = len(str_x)
        lim = str(2**31)
        #Reverse
        str_x = ''.join(str_x[i] for i in range(N-1,-1,-1))
        
        #If not inside limit, return zero
        if len(str_x) == len(lim):
            for i,j in zip(str_x,lim):
                if int(i) < int(j):
                    break
                elif int(i) == int(j):
                    continue
                else:
                    return 0
        
        if neg:
            str_x = '-'+str_x
            
        return int(str_x)
            