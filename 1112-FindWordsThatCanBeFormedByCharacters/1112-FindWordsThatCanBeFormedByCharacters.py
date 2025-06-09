# Last updated: 6/9/2025, 5:25:50 PM
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # check if word in list of words can be made from characters in chars each once 
        # return sum of lengths of all good words 
        # if each letter in word is in chars, remove it from chars 
        # freq map for each word? 
        # how many times each character occurs in char
        # key value, for each letter in word, check that letter, value =< charsmap

        # length 
        length = 0 
        # freq map 
        freq = defaultdict(int)

        # map chars 
        for c in chars: 
            freq[c] += 1
        
        # check each word
        for word in words: 
            # check if char in word shows up more than in char - invalid 
            for char in word: 
                if word.count(char) > freq[char]:
                    break
            # if char in word shows up less or eq to char in given 
            else:
                #add on length
                length += len(word)
        
        return length
        
    

                 
        