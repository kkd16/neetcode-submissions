class WordDictionary:
    
    class Node:
        def __init__(self):
            self.children = {}
            self.end = False

    def __init__(self):
        self.children = {}
        self.end = False
   

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = self.Node()
            curr = curr.children[c]

        curr.end = True

    def dfs(self, word, index, curr):
        if index == len(word):
            return curr.end
        
        c = word[index]
        if c != '.' and c in curr.children:
            return self.dfs(word, index + 1, curr.children[c])
        elif c == '.':
            for child in curr.children.values():
                if self.dfs(word, index + 1, child):
                    return True
        
        return False
            

    def search(self, word: str) -> bool:
        return self.dfs(word, 0, self)
        
        
