# Last updated: 11/1/2025, 4:58:44 PM
class Solution:
    def mostCommonWord(self, para: str, ban: List[str]) -> str:
        s = "".join([i.lower() if i.isalnum() else ' ' for i in para])
        word = s.split()
        cou = {}
        ban_set = set(ban)

        for i in word:
            if i not in ban_set:
                cou[i] = cou.get(i, 0) + 1
                        
        return max( cou.items() , key=operator.itemgetter(1) )[0]
