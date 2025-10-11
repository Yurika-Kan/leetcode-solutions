# Last updated: 10/11/2025, 1:45:51 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Understand: given an int, return true / false if it reads same forwards & backwards
        # input: x int, output: boolean 
        # edge: 
        # x = 1 -> true anytime len(x) == 1
        # x = -1 -> false anytime x < 0
        # x = 123321 -> false
        # x = 12321 -> true 

        # Match: 
        # two pointer, reverse - string
        # - int 

        #strX = list(x)

        #if len(strX) == 1: 
        #    return True
        
        # reversed() -> iterator 
        # iterator -> list or str

        # return strX == ''.join(reversed(strX))
        #return strX == list(reversed(strX))

        # no string conversion implementation
        if x < 0: 
            return False
        
        # x   = 121 
        # div = 100
        div = 1
        while x >= 10 * div:
            div *= 10
        
        while x: 
            # 121 % 10 = 1
            right = x % 10
            # 121 // 100 = 1
            left = x // div

            if left != right: 
                return False
            
            # (chop left) // chop right
            # 121 % 100 = 21 // 10 = 2
            x = (x % div) // 10
            
            # update chop off 2 digits
            div = div / 100

        return True
        
        # Time C: O(n) linear
        # Space C: O(n) holding x 