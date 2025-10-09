# Last updated: 10/9/2025, 1:12:54 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Understand: given a string
        # return len of longest substring 
        # created with at most k replacements

        # cases: 
        # XYYX --> XXXX / YYYY
        # X --> 1
        # VYUD --> 4 (len of s / k)

        # notes: always upper case

        # brute force: check every char -> substring

        # replace with more freq char
        # Match: sliding window, freq map 
        # Plan: 

        # edge
        if len(s) == 1:
            return 1
        
        # window & count freq at same time
        # freq of char in this curr window 
        
        freqMap = {}
        result = 0
        l = 0

        # loop by right pointer 
        for r in range(len(s)):
            # get that charc val or default 
            freqMap[s[r]] = 1 + freqMap.get(s[r], 0) #bounded by 26 abcs 

            # while window is not valid - shift left
            # window - maxfreq = # of replacements we have to do > allowed
            # any smaller window would only decrease max possible len
            while (r - l + 1) - max(freqMap.values()) > k: 
                # decrement count of left char in curr window 
                freqMap[s[l]] -= 1
                l += 1
            # update max w window size or prev max
            result = max(result, r - l + 1)

        return result

    # Time C: O(n)
    # Space C: O(1) # counts of charc in curr window