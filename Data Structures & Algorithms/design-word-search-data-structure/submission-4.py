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

    def search(self, word: str) -> bool:
        
        def dfs(j, child):
            cur = child

            for i in range(j, len(word)):
                c = word[i]

                if c == '.':
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False

                    cur = cur.children[c]

            return cur.end 
    
        return dfs(0, self.root)
        
