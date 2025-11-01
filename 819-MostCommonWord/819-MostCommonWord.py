# Last updated: 11/1/2025, 4:32:41 PM
import re 
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Understand: given a str of characters w uppercase, lowercase, punctuations, return word that is most common & not banned
        # lowercase all
        # looking for word% -surrounded by other punctuation

        # edge: 
        # no most common word -> ""
        
        # Match: 
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



'''
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

