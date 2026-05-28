class WordDictionary:

    class TrieNode:
        def __init__(self):
            self.children = {}
            self.end = False

    def __init__(self):
        self.root = self.TrieNode()
        

    def addWord(self, word: str) -> None: 
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = self.TrieNode()
            cur = cur.children[c]

        cur.end = True      

    def _search(self, word: str, start: TrieNode) -> bool:
        cur = start

        for i, c in enumerate(word):

            if c != '.' and c not in cur.children:
                return False

            if c == '.':
                for nc in cur.children:
                    if self._search(word[i+1:], cur.children[nc]):
                        return True
                return False
            else:
                cur = cur.children[c]

        return cur.end 

    def search(self, word: str) -> bool:
        return self._search(word, self.root)

        
