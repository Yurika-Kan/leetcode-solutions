# Last updated: 8/11/2025, 3:51:09 PM
# singular node class
class TrieNode:
    def __init__(self):
        # hashmap!
        self.children = {}
        self.end_of_word = False

# tree class
class Trie:
    # initializes trie
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        # recursively iterate levels
        curr = self.root
        
        for cha in word: 
            # if char not in tree then add 
            if cha not in curr.children: 
                curr.children[cha] = TrieNode()
            # if char in tree then traverse to next level w next char
            curr = curr.children[cha]
        curr.end_of_word = True

    # true if word is in prefix tree - until reach None
    def search(self, word: str) -> bool:
        curr = self.root

        for cha in word: 
            if cha not in curr.children: 
                return False
            # if char in tree then next level 
            curr = curr.children[cha]
        # check if valid word
        return curr.end_of_word
        
    # true if prefix is in tree - until prefix is there, no need to go to None node 
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for cha in prefix: 
            if cha not in curr.children: 
                return False
            curr = curr.children[cha]
        # any prefix 
        return True
        
    # Time Complexity: O(n) where n is len of string
    # Space Complexity: O(t) where t is num of TrieNodes


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)