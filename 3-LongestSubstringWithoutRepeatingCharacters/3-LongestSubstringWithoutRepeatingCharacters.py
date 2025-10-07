# Last updated: 10/7/2025, 11:38:58 AM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Understand: find largest substring of characters w no repeating chars
        # input: string - case sensitive? spaces? no chars?
        # output: number representing length of longest substring
        # edge cases
        if not s: 
            return 0
        # Match: use sliding window w two ptrs l & r
        # use set to track uniq chars in current window
        
        # store unique chars
        char_set = set()
        l = 0
        result = 0


        for r in range(len(s)):
            # theres a dupe. ok next
            # clears the array until no duplicates
            # if s[r] already in window shrink window from left
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            # substring has no duplicates
            # unique set of characters at a time
            char_set.add(s[r])
            result = max(result, r - l + 1)
        return result


# Time C: O(n) since each char added and removed at most once
# Space C: O(min(n, a)) where a is charset size (26 if lowercase ascii)