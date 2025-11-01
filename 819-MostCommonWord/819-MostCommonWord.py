# Last updated: 11/1/2025, 7:22:15 PM
import re 
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Understand: given a str of characters w uppercase, lowercase, punctuations, return word that is most common & not banned
        # lowercase all
        # looking for word% -surrounded by other punctuation

        # edge: 
        # no most common word -> ""
        
        # Match: splicing, lower, alnum, keys
        # cleans paragaph to not include punctuality 
        # over each char
        cleanedP = "".join([char.lower() if char.isalnum() else ' ' for char in paragraph])
        # default split chars to words
        words = cleanedP.split()
        freqMap = {}

        for word in words:
            # r u banned? if not join us!
            if word not in banned:
                freqMap[word] = freqMap.get(word, 0) + 1
        
        # return the key, val item with highest val (freq)
        maxPair = max(freqMap.items(), key=lambda item: item[1]) 

        return maxPair [0]
        
# Time C: O(n + m) where n is len of words in paragraph & m is len of words in banned
# Space C: O(n)

'''
one pass solution
# one pass processing each char with most common accumulator
        # case 1: middle of word ->  wadd word to word buffer
        # case 2: middle of words in between (space or punc) -> check if word in banned, update freq of word, update most common word so far
        res = ""
        maxCount = 0
        wordCount = {}
        wordBuffer = []

        for idx, char in enumerate(paragraph):
            # char -> word 
            # r u punctuation?
            if char.isalnum():
                # ok, let's lowercase u
                wordBuffer.append(char.lower())
                if idx != len(paragraph) - 1: 
                    continue
            
            # u r space / punc
            if len(wordBuffer) > 0: 
                word = "".join(wordBuffer)
                if word not in banned:
                    wordCount[word] = wordCount.get(word, 0) + 1
                    if wordCount[word] > maxCount: 
                        maxCount = wordCount[word]
                        res = word
                # reset for next round
                wordBuffer = []
            
        return res

# Time C: O(n + m) where n is len of paragraph, m is len of banned
# Space C: O()

naive solution
        # paragraph -> splice by ' ' -> list of items - lowercase, punctuality (just remove)
        #paragraph.splice()
        words = re.findall(r'\w+|[.,!?;]', paragraph)
        #words.removeAll
        punc = ["!", "?" ,"," , ";", "."]
        for word in words: 
            if word in punc: 
                words.remove(word)
        # dict - counter import - freq map 
        freqMap = {}
        for word in words: 
            word = word.lower()
            if word not in banned:
                freqMap[word] = freqMap.get(word, 0)+1
        
        # sort it descending 
        sortedWords = sorted(freqMap.items(), key=lambda item: item[1], reverse=True)
        # iterate, return if not in banned 

        return sortedWords[0][0]

'''

