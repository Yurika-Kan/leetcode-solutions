# Last updated: 11/1/2025, 7:19:35 PM
# Trie - prefix tree 

# TrieNode - node with children + end marker bool 
# node = {'i', children:{}, True}
class Word: 

    def __init__(self):
        self.children = {}
        self.isEnd = False

# Trie - set root node & update to traverse
class WordDictionary:

    def __init__(self):
        self.root = Word()

    def addWord(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.children: 
                node.children[letter] = Word()
            node = node.children[letter]
        node.isEnd = True
        

    def search(self, word: str) -> bool:
        def dfs(j, root):
            node = root
            # recursive
            for i in range(j, len(word)): 
                letter = word[i]

                if letter == '.':
                    for child in node.children.values():
                        if dfs(i + 1, child): 
                            return True
                    return False
                # return node.children[].children[].isEnd
                # iterative
                if letter not in node.children: 
                    return False 
                node = node.children[letter]
            return node.isEnd
        return dfs(0, self.root)
    
# Time C: O(n)
# Space C: O(t + n) where t is num of TrieNodes created in Trie