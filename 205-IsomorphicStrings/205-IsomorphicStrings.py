# Last updated: 11/1/2025, 4:59:19 PM
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


        