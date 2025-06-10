# Last updated: 6/9/2025, 5:25:44 PM
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # length check 
        # add char & index in map if not 
        # compare index # of same char in each map 
        if len(s) != len(t):
            return false
        dictS = {}
        dictT = {}
        for i in range(0, len(s)):
            if not s[i] in dictS:
                dictS[s[i]] = i
            if not t[i] in dictT:
                dictT[t[i]] = i
            if dictS[s[i]] != dictT[t[i]]:
                return False
        return True


        